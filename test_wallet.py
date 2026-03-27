from wallet import Novcanik

def test_pocetno_stanje():
    moj_novcanik = Novcanik(100)
    assert moj_novcanik.stanje == 100

def test_dodavanje_novca():
    moj_novcanik = Novcanik(50)
    moj_novcanik.dodaj_novac(30)
    assert moj_novcanik.stanje == 80

def test_potrosnja_novca():
    moj_novcanik = Novcanik(100)
    moj_novcanik.potrosi_novac(40)
    assert moj_novcanik.stanje == 60