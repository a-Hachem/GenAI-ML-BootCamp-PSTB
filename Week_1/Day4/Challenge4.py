class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []  # Liste des éléments à paginer
        self.pageSize = int(pageSize)  # Convertir en int au cas où ce serait un float
        self.totalPages = max(1, (len(self.items) + self.pageSize - 1) // self.pageSize)  # Nombre total de pages
        self.currentPage = 1

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]  # Retourne la liste des éléments visibles sur la page actuelle

    def nextPage(self):
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        return self  # Permet d'enchaîner les appels : p.nextPage().nextPage()

    def prevPage(self):
        if self.currentPage > 1:
            self.currentPage -= 1
        return self

    def firstPage(self):
        self.currentPage = 1
        return self

    def lastPage(self):
        self.currentPage = self.totalPages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum) 
        if pageNum < 1:
            self.currentPage = 1
        elif pageNum > self.totalPages:
            self.currentPage = self.totalPages
        else:
            self.currentPage = pageNum
        return self

# Exemple d'utilisation
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  

p.nextPage()

print(p.getVisibleItems())  

p.lastPage()

print(p.getVisibleItems())  

