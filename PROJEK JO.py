laporan = []
sudah_wawancara = set()
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def intro():
    nama = input ("Masukkan nama anda: ")
    print (f"Selamat datang, Detektif {nama}.")
    print ("Anda ditugaskan menyelidiki kasus ORION STAGE mengenai seorang idol ternama Lin Yue.")
    print ("Yang dikabarkan menghilang secara misterius pada pukul 21.55.")
    input ("\nTekan ENTER untuk memulai penyelidikan...")
    clear()


def narasi_awal():
    print ("""Malam itu seharusnya menjadi puncak konser terbesar tahun ini.
Lampu panggung menyala. Musik menggelegar.
Namun beberapa menit sebelum penampilan terakhirnya, Lin Yue menghilang.
Tidak ada tanda perlawanan. Tidak ada saksi yang melihat jelas. Hanya satu anting yang ditemukan di belakang panggung.

Manajer mengatakan ia sedang mengurus teknis.
Seorang penggemar fanatik terlihat di area VIP.
Dan seorang sahabat lama hadir sebagai tamu khusus malam itu.

Publik gempar. Media berspekulasi.
Dan hingga saat ini, Lin Yue masih belum ditemukan.""")



def menu_utama():
    while True:
        print ("\nPILIH TINDAKAN YANG INGIN ANDA LAKUKAN: ")
        print ("a. Wawancara Suspect")
        print ("b. Lihat Laporan")
        print ("c. Simpan Laporan")
        print ("d. Pilih Pelaku")
        print ("e. Keluar")

        menu = input("Pilih menu: ").lower()
        clear()

        if menu == "a":
            wawancara()
        elif menu == "b":
            lihat_laporan()
        elif menu == "c":
            simpan_laporan()
        elif menu == "d":
            pilih_pelaku()
        elif menu == "e":
            print ("Program selesai.")
            break
        else:
            print ("Menu tidak valid.")
            break  


def wawancara():
    print (" Pilih suspect untuk diwawancarai:")
    print ("1. Sasaeng")
    print ("2. Teman Lama (Rui san)]")
    print ("3. Manager (Zen len)")

    pilih = input("Pilihan (1-3): ")
    clear()

    if pilih == "1":
        suspect = "Sasaeng" 
        print (
            "Seorang penggemar fanatik yang sudah lama mengikuti Lin Yue."
            "\nIdol sempat menulis di catatan pribadinya bahwa ia merasa diawasi."
            "\nDi kamar sasaeng ditemukan foto-foto Lin Yue dengan tanda merah, list jadwal konser, dan tiket VIP."
            '\n"Aku memang fans beratnya. Tapi aku nggak akan pernah menyakitinya."'
            '\n"Aku cuma ingin dekat dengannya. \nDan waktu dia istirahat, aku ada di area VIP. Banyak orang lihat aku di sana."'
            )
        
        point_laporan = (
            "- Mengaku fans berat\n"
            "- Terlihat di area VIP\n"
            "- Menyangkal penculikan\n"
            "- terlihat sangat gugup dengan tangan gemetar\n"
        )

    elif pilih == "2":
        suspect = "Teman Lama (Rui san)"
        print (
            "Namanya Rui san. Teman semasa sekolah Lin Yue yang juga pernah menjadi korban bullying sang idol."
            "\nSaat itu, keluarga Lin Yue meminta damai secara rahasia dengan memberikan uang tutup mulut kepada orang tuanya."
            "\nNamun beberapa tahun terakhir mereka terlihat akrab kembali dan sering tampil bersama di media,"
            "menciptakan citra 'persahabatan yang telah berdamai.'"
            '\n"Ya, kami memang punya masa lalu yang buruk. Tapi kami sudah menyelesaikannya."'
            '\n"Orang bisa berubah, Detetktif. Aku nggak punya alasan buat melakukan hal seperti ini.."'
            )

        point_laporan = (
    "- Memiliki konflik masa lalu\n"
    "- Emosi tidak stabil\n"
    "- Membantah sebagai pelaku\n"
    "- Saat wawancara, terlihat hanya mengenakan satu anting\n"
    "- Sisi lainnya tertutup rambut dan tidak dijelaskan saat ditanya\n"
)
        

    elif pilih == "3":
        suspect = "Manager (Zen len)"
        print (
            "Manager Zen Len adalah orang yang telah mendampingi Lin Yue selama lima tahun."
            "\nMengatur jadwal, kontrak, hingga akses backstage."
            "\nNamun belakangan ini, mereka  sering berselisih karena Lin Yue ingin mengurangi jadwal konsernya yang terlalu padat."
            '\n"Aku sedang mengurus koordinasi teknis. Konser sebesar ini butuh kontrol penuh."'
            '\n"Jangan asal menyimpulkan hanya karena aku punya akses, tugas saya melindungi artis saya, dan saya tidak punya alasan menyakitinya."'
            '\n"Justru saya yang paling dirugikan kalau dia hilang..."'
            )

        point_laporan = (
            "- Ia satu‑satunya yang tahu pasti waktu jeda dan perubahan jadwal mendadak malam itu.\n"
            "- Bertanggung jawab atas teknis\n"
            "- Sikap terlalu tenang\n"
            "- Punggung tangannya tanpak di tutupi plester luka.\n"
        )

    else:
        print ("Pilihan tidak valid.")
        return

    if suspect in sudah_wawancara:
        print ("Suspect ini sudah diwawancarai.")
        return

    laporan.append(f"{suspect}:\n{point_laporan}")
    sudah_wawancara.add(suspect)


def lihat_laporan():
    print ("\n LAPORAN INVESTIGASI ")
    if not laporan:
        print ("Belum ada laporan.")
    else:
        for i, l in enumerate(laporan, 1):
            print (f"\nLaporan {i}")
            print (l)


def simpan_laporan():
    if not laporan:
        print ("Tidak ada laporan untuk disimpan.")
        return

    with open ("laporan_orion_stage.txt", "w", encoding="utf-8") as file:
        for l in laporan:
            file.write (l + "\n")

    print ("Laporan berhasil disimpan.")

def pilih_pelaku():
    if len (sudah_wawancara) < 3:
        print ("Wawancarai semua suspect terlebih dahulu.")
        return

    print ("\nSiapa pelaku sebenarnya?")
    print ("1. Sasaeng")
    print ("2. Teman Lama (Rui san)")
    print ("3. Manager (Zen len)")

    pilih = input ("Pilihan: ")
    clear ()

    if pilih == "1":
        print (
            '"Aku bukan pelakunya detektif! Sungguh..."'
            '\n"Mana mungkin aku menyakiti seseorang yang telah membantuku kembali merasa hidup! Aku sangat mencintainya..sangat..."'
            )
        print (
            "Detektif tidak menghiraukan pembelaannya, ia hanya diam dan menggeleng pelan. "
            "\nPolisi dengan cepat mangambil alih. Memasang borgol pada kedua tangan sasaeng, lalu membawanya menuju mobil."
            )
        
        print ("\n HASIL INVESTIGASI")
        print ("""Kamu gagal. Sasaeng bukanlah pelaku sebenarnya. Coba analisis kembali petunjuk yang ada.""")

    elif pilih == "2":
        print ('"Aku tahu… aku terlihat paling masuk akal untuk dicurigai. Tapi marah bukan berarti aku membunuhnya."')
        print ("Polisi memasang borgol pada kedua tangan Rui San, lalu membawanya menuju mobil.")
        print (" ")
        print ("HASIL INVESTIGASI")
        print ("Kamu gagal. Teman lama bukanlah pelaku sebenarnya. Coba analisis kembali petunjuk yang ada.")
        
    elif pilih == "3":
        print ('"Saya membentuknya dari nol. Saya yang membuat dunia mengenalnya."')
        print ('"Jadi saya juga yang berhak menentukan bagaimana kisahnya berakhir. "')
        print (
            "Seisi ruangan terkejut mendengar pengakuan kejam sang manager. " 
            "\nTanpa menunggu lama, polisi bergerak mengambil alih, memasang borgol, lalu membawanya."
            )
        print ("\n HASIL INVESTIGASI")
        print ("\n Kamu berhasil. Manager adalah pelakunya.")

        print (
            "Ia mengaku bahwa terus-menerus diancam oleh Lin Yue dengana rahasia buruk masa lalunya."
            "\nKarena takut karirnya hancur, ia nekat meracuni Lin Yue dengan zat sianida."
            )

        print (
            "Setelah itu, Tubuh Lin Yue ditemukan tewas dengan mulut berbusa di dalam bagasi mobil pribadinya."
            "\nDan fakta bahwa Zen Len adalah satu-satunya orang yang mengetahui bahwa Lin Yue membawa mobil pribadi pada konser kali ini,"
            "\nmenjadikannya pelaku yang tak terbantahkan.."
            )
    else:
        print ("Pilihan tidak valid.")


intro()
narasi_awal()
menu_utama()