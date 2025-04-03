import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    RocCurveDisplay,
    PrecisionRecallDisplay,
)


def main():
    # App title and description
    st.title("🍄 Mushroom Classification App")
    st.markdown("""
        **Are your mushrooms edible or poisonous?**  
        This app uses machine learning to classify mushrooms based on their features.  
        Choose a classifier, adjust hyperparameters, and evaluate the results!
    """)

    # Sidebar
    st.sidebar.title("Options")
    st.sidebar.markdown("Configure the classifier and metrics.")

    @st.cache_data(persist=True)
    def load_data():
        """Load and preprocess the mushroom dataset."""
        data = pd.read_csv('mushrooms.csv')
        label = LabelEncoder()
        for col in data.columns:
            data[col] = label.fit_transform(data[col])
        return data

    @st.cache_data(persist=True)
    def split(df):
        """Split the dataset into training and testing sets."""
        y = df.type
        x = df.drop(columns=['type'])
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        return x_train, x_test, y_train, y_test

    def plot_metrics(metrics_list, model, x_test, y_test, y_pred):
        """Plot selected evaluation metrics."""
        if 'Confusion Matrix' in metrics_list:
            st.subheader("Confusion Matrix")
            cm = confusion_matrix(y_test, y_pred)
            fig, ax = plt.subplots()
            ConfusionMatrixDisplay(cm).plot(ax=ax)
            st.pyplot(fig)

        if 'ROC Curve' in metrics_list:
            st.subheader("ROC Curve")
            fig, ax = plt.subplots()
            RocCurveDisplay.from_estimator(model, x_test, y_test, ax=ax)
            st.pyplot(fig)

        if 'Precision-Recall Curve' in metrics_list:
            st.subheader("Precision-Recall Curve")
            fig, ax = plt.subplots()
            PrecisionRecallDisplay.from_estimator(model, x_test, y_test, ax=ax)
            st.pyplot(fig)

    def plot_feature_importance(model, feature_names):
        """Plot feature importance for Random Forest using matplotlib."""
        if hasattr(model, 'feature_importances_'):
            st.subheader("Feature Importance")
            importance = model.feature_importances_
            importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': importance
            }).sort_values(by='Importance', ascending=False)

            fig, ax = plt.subplots(figsize=(10, 6))
            ax.barh(importance_df['Feature'], importance_df['Importance'])
            ax.set_xlabel("Importance")
            ax.set_ylabel("Feature")
            ax.set_title("Feature Importance")
            st.pyplot(fig)
        else:
            st.warning("Feature importance is not available for this model.")

    # Load and split data
    df = load_data()
    x_train, x_test, y_train, y_test = split(df)
    class_names = ['edible', 'poisonous']

    # Sidebar options
    st.sidebar.subheader("Choose Classifier")
    classifier = st.sidebar.selectbox(
        "Classifier",
        ("Support Vector Machine (SVM)", "Logistic Regression", "Random Forest")
    )

    # Classifier-specific hyperparameters
    if classifier == "Support Vector Machine (SVM)":
        st.sidebar.subheader("SVM Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C')
        kernel = st.sidebar.radio("Kernel", ("rbf", "linear"), key='kernel')
        gamma = st.sidebar.radio("Gamma (Kernel Coefficient)", ("scale", "auto"), key='gamma')

    elif classifier == "Logistic Regression":
        st.sidebar.subheader("Logistic Regression Hyperparameters")
        C = st.sidebar.number_input("C (Regularization parameter)", 0.01, 10.0, step=0.01, key='C_LR')
        max_iter = st.sidebar.slider("Maximum number of iterations", 100, 500, key='max_iter')

    elif classifier == "Random Forest":
        st.sidebar.subheader("Random Forest Hyperparameters")
        n_estimators = st.sidebar.number_input("Number of trees in the forest", 100, 5000, step=10, key='n_estimators')
        max_depth = st.sidebar.number_input("Maximum depth of the tree", 1, 20, step=1, key='max_depth')
        bootstrap = st.sidebar.radio("Bootstrap samples when building trees", (True, False), key='bootstrap')

    # Metrics selection
    metrics = st.sidebar.multiselect(
        "What metrics to plot?",
        ('Confusion Matrix', 'ROC Curve', 'Precision-Recall Curve')
    )

    # Classify button
    if st.sidebar.button("Classify", key='classify'):
        st.subheader(f"{classifier} Results")

        try:
            # Train the selected model
            if classifier == "Support Vector Machine (SVM)":
                model = SVC(C=C, kernel=kernel, gamma=gamma)
            elif classifier == "Logistic Regression":
                model = LogisticRegression(C=C, max_iter=max_iter)
            elif classifier == "Random Forest":
                model = RandomForestClassifier(
                    n_estimators=n_estimators,
                    max_depth=max_depth,
                    bootstrap=bootstrap,
                    n_jobs=-1
                )

            model.fit(x_train, y_train)
            y_pred = model.predict(x_test)

            # Display results
            accuracy = model.score(x_test, y_test)
            st.write(f"**Accuracy:** {accuracy:.2f}")
            st.write(f"**Precision:** {precision_score(y_test, y_pred, labels=class_names, average='weighted'):.2f}")
            st.write(f"**Recall:** {recall_score(y_test, y_pred, labels=class_names, average='weighted'):.2f}")
            st.write(f"**F1-Score:** {f1_score(y_test, y_pred, labels=class_names, average='weighted'):.2f}")

            # Plot selected metrics
            plot_metrics(metrics, model, x_test, y_test, y_pred)

            # Plot feature importance for Random Forest
            if classifier == "Random Forest":
                plot_feature_importance(model, x_train.columns)

            # Download results
            results_df = pd.DataFrame({
                'Actual': y_test,
                'Predicted': y_pred
            })
            st.download_button(
                label="Download Results as CSV",
                data=results_df.to_csv(index=False).encode('utf-8'),
                file_name='mushroom_classification_results.csv',
                mime='text/csv'
            )

        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Show raw data option
    if st.sidebar.checkbox("Show raw data", False):
        st.subheader("Mushroom Dataset")
        st.write(df)


if __name__ == '__main__':
    main()