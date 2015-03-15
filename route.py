import handlers

routers = [
	(r"/", "handlers.account.WelcomeHandler"),
	(r"/login", "handlers.account.LoginHandler"),
	(r"/logout", "handlers.account.LogoutHandler"),
	(r"/register", "handlers.account.RegisterHandler")
]