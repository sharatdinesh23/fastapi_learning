class DatabaseSession:
    
    def __enter__(self):
        print("Database Connected")
        return self
    
    def __exit__(self, exc_type, exc, tb):
        print("Database Closed")
        
    