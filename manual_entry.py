# import pandas as pd
#
# # bikin list kosong untuk menampung data yang diinput
# data_list = []
#
# # loop untuk input data berkali kali
# while True:
#     print("\nMasukkan data baru (atau ketik 'selesai' untuk berhenti)")
#
#     product_title = input("product_title: ")
#     if product_title.lower() == "selesai":
#         break
#
#     cost = input("cost: ")
#     stock_quantity = input("stock_quantity: ")
#     category = input("category: ")
#     brand = input("brand: ")
#     supplier = input("supplier: ")
#
#     # ⬇️ Tambahkan data ke list
#     data_list.append({
#         "product_title": product_title,
#         "cost": cost,
#         "stock_quantity": stock_quantity,
#         "category": category,
#         "brand": brand,
#         "supplier": supplier
#     })
#
# # ubah ke DataFrame
# df = pd.DataFrame(data_list)
# df.to_csv("data_manual.csv", index=False)
#
# print("\nData berhasil disimpan ke 'data_manual.csv'")
#


import pandas as pd

data_list = []

while True:
    print("\nMasukkan data baru (atau ketik 'selesai' untuk berhenti)")

    product_title = input("product_title: ")
    if product_title.lower() == "selesai":
        break

    cost = input("cost: ")
    stock_quantity = input("stock_quantity: ")
    category = input("category: ")
    brand = input("brand: ")
    supplier = input("supplier: ")

    # tampilkan hasil input untuk dikonfirmasi
    print("\nCek kembali data yang kamu masukkan:")
    print(f"Product Title : {product_title}")
    print(f"Cost          : {cost}")
    print(f"Stock Quantity: {stock_quantity}")
    print(f"Category      : {category}")
    print(f"Brand         : {brand}")
    print(f"Supplier      : {supplier}")

    konfirmasi = input("Apakah data sudah benar? (y/n): ").lower()
    if konfirmasi == "y":
        data_list.append({
            "product_title": product_title,
            "cost": cost,
            "stock_quantity": stock_quantity,
            "category": category,
            "brand": brand,
            "supplier": supplier
        })
        print("✅ Data disimpan.")
    else:
        print("↩️ Silakan input ulang data ini.")

df = pd.DataFrame(data_list)
df.to_csv("data_manual.csv", index=False)
print("\nData berhasil disimpan ke 'data_manual.csv'")