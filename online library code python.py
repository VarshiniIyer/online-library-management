import streamlit as st
import mysql.connector
import pandas as pd

# Database connection
def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='library_management'
    )

# Function to add a new book
def add_book(title, author, isbn):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, isbn) VALUES (%s, %s, %s)", (title, author, isbn))
    conn.commit()
    conn.close()

# Function to view all books
def view_books():
    conn = create_connection()
    df = pd.read_sql("SELECT * FROM books", conn)
    conn.close()
    return df

# Streamlit app layout
def main():
    st.title("Library Management System")

    menu = ["Add Book", "View Books"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.subheader("Add a New Book")
        title = st.text_input("Title")
        author = st.text_input("Author")
        isbn = st.text_input("ISBN")
        if st.button("Add Book"):
            add_book(title, author, isbn)
            st.success(f"Added {title} by {author}")

    elif choice == "View Books":
        st.subheader("Book List")
        df = view_books()
        st.dataframe(df)

if __name__ == '__main__':
    main()
