from models.item import Item

class InventoryList:
    def __init__(self):
        self.head = None

    def add_item(self, id_barang, nama, kategori, harga, stok):
        new_item = Item(id_barang, nama, kategori, harga, stok)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    def display_items(self):
        if self.head is None:
            print("Tidak ada barang di inventory.")
            return
        current = self.head
        while current:
            print(f"ID: {current.id_barang} | Nama: {current.nama} | Kategori: {current.kategori} | Harga: {current.harga} | Stok: {current.stok}")
            current = current.next

    def find_item_by_name(self, nama):
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                return current
            current = current.next
        return None

    def update_item(self, id_barang, nama=None, kategori=None, harga=None, stok=None):
        current = self.head
        while current:
            if current.id_barang == id_barang:
                if nama:
                    current.nama = nama
                if kategori:
                    current.kategori = kategori
                if harga is not None:
                    current.harga = harga
                if stok is not None:
                    current.stok = stok
                return True
            current = current.next
        return False

    def delete_item(self, id_barang):
        current = self.head
        prev = None
        while current:
            if current.id_barang == id_barang:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def cek_stok_rendah(self, ambang_batas=5):
        current = self.head
        print("\n=== NOTIFIKASI STOK RENDAH ===")
        stok_rendah = False
        while current:
            if current.stok <= ambang_batas:
                print(f"⚠️  {current.nama} stok tersisa {current.stok}")
                stok_rendah = True
            current = current.next
        if not stok_rendah:
            print("Semua stok dalam kondisi aman.")

    def sortir_barang(self, kunci='nama'):
        data = []
        current = self.head
        while current:
            data.append(current)
            current = current.next

        if kunci == 'nama':
            data.sort(key=lambda x: x.nama.lower())
        elif kunci == 'harga':
            data.sort(key=lambda x: x.harga)
        elif kunci == 'stok':
            data.sort(key=lambda x: x.stok)

        print(f"\n=== Daftar Barang diurutkan berdasarkan {kunci.capitalize()} ===")
        for item in data:
            print(f"ID: {item.id_barang} | Nama: {item.nama} | Harga: {item.harga} | Stok: {item.stok}")
