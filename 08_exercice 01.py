livres=[{"titre":"Python débutant","auteur":"Tshitende","année":2020},
       {"titre":"maitriser Python","auteur":"Ngandu","année":2022},
       {"titre":"Python avancé","auteur":"Ryan","année":2024}]
print("livre publiés aprèes 2021")
for livre in livres:
    if livre["année"] > 2021:
        print(f"{livre['titre']} ({livre['année']}) de {livre['auteur']}")
        


