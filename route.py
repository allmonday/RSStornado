import handlers

routers = [
	(r"/", "handlers.account.WelcomeHandler"),
	(r"/login", "handlers.account.LoginHandler"),
	(r"/logout", "handlers.account.LogoutHandler"),
	(r"/register", "handlers.account.RegisterHandler"),
    (r"/api/blog", "handlers.blog.BlogHandler"),
    (r"/api/test", "handlers.test.TestHandler")
]
