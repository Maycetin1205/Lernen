# -*- coding: utf-8 -*-
import subprocess

html_content = '''<section class="kapitel" id="a5" data-gruppe="A">

<header class="kapitel-kopf">
  <p class="kapitel-nr">A5 · Verfahren</p>
  <h2>Strom und Energiekosten</h2>
  <p class="kam-dran">Kam dran: <span>AP1 Herbst 2021, 2.1, 2.2, 2.4 (14 P)</span> · <span>AP1 Frühjahr 2024, 3.7, 3.8 (7 P)</span> · <span>AP1 Herbst 2025, 3.5, 3.6 (5 P)</span></p>
  <label class="sitzt"><input type="checkbox" data-key="a5"> Sitzt</label>
</header>

<section id="a5-worum">
  <h3>Worum es geht</h3>
  <p>Ein IT-Systemhaus modernisiert die Arbeitsplatz-Hardware einer Ingenieurgesellschaft mit 80 Hochleistungs-Workstations und zwei CAD-Plottern. Vor der Bestellung muss die Projektleitung berechnen, welche Netzteilleistung für die Rechner unter Volllast erforderlich ist und welche jährlichen Stromkosten durch den Einsatz energieeffizienter Netzteile mit 80-PLUS-Zertifizierung eingespart werden können. Falsch dimensionierte Netzteile führen bei Spitzenlast zu Systemabstürzen, während ineffiziente Netzteile die Betriebskosten und die Wärmeentwicklung im Büro unnötig in die Höhe treiben. In der IHK-Abschlussprüfung werden regelmäßig Formeln zur elektrischen Leistung, Jahresenergiekosten, Netzteildimensionierungen mit Sicherheitsreserven und Amortisationszeiten gefordert.<sup class="q"><a href="#a5-q1" title="Hering Physik">1</a></sup></p>
</section>

<section id="a5-begriffe">
  <h3>Begriffe</h3>

  <dl class="begriff" id="a5-begriff-leistung">
    <dt>Elektrische Leistung, Spannung und Stromstärke <span class="en">(Electric Power, Voltage, Current)</span></dt>
    <dd><span class="label">Theorie</span><p>Die elektrische Leistung P (in Watt, W) ist das Produkt aus der anliegenden elektrischen Spannung U (in Volt, V) und der fließenden Stromstärke I (in Ampere, A): P = U * I.<sup class="q"><a href="#a5-q1" title="Hering Physik">1</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Ein PC-Netzteil an der europäischen Netzspannung von 230 V nimmt bei einem gemessenen Strom von 1,5 A eine elektrische Leistung von 345 Watt auf.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>P = U * I. Spannung ist der Druck im Netz (Volt), Stromstärke die Menge der Ladungsträger (Ampere), Leistung die erbrachte Arbeit pro Sekunde (Watt).</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Gegeben sind meist zwei Größen (z. B. 230 V und 460 W); gesucht ist die Stromstärke (I = P / U = 2 A).</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-arbeit">
    <dt>Elektrische Arbeit und Kilowattstunde <span class="en">(Electric Energy, Kilowatt-Hour)</span></dt>
    <dd><span class="label">Theorie</span><p>Die über eine Zeitspanne t verrichtete elektrische Energie E ist das Produkt aus Leistung P und Betriebsdauer t: E = P * t, gemessen in Wattstunden (Wh) oder Kilowattstunden (kWh mit 1 kWh = 1.000 Wh).<sup class="q"><a href="#a5-q2" title="Europa IT-Handbuch">2</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Stromversorger rechnen die gelieferte Energie verbrauchsabhängig in Kilowattstunden ab.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>Leistung (Watt) ist der Momentanwert; Energie (kWh) ist die kumulierte Arbeit über die Zeit (Leistung mal Stunden).</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Wattangaben müssen vor der Multiplikation mit den Betriebsstunden zwingend durch 1.000 geteilt werden, um Kilowattstunden zu erhalten.</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-stromkosten">
    <dt>Stromkostenberechnung <span class="en">(Electricity Cost Calculation)</span></dt>
    <dd><span class="label">Theorie</span><p>Die Gesamtkosten für elektrische Energie ergeben sich aus der verbrauchten Arbeit in kWh multipliziert mit dem vertraglichen Stromarbeitspreis in Euro pro Kilowattstunde: Kosten = E[kWh] * Arbeitspreis.<sup class="q"><a href="#a5-q3" title="BNetzA Monitoring">3</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Ermöglicht den kaufmännischen Vergleich von Hardwarevarianten hinsichtlich ihrer Betriebskosten über mehrere Jahre.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>Betriebs- und Standby-Phasen müssen getrennt berechnet und anschließend addiert werden.</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Klassische Prüfungsaufgabe: Berechnung der jährlichen Stromkosten bei vorgegebenen Betriebsstunden pro Tag und Arbeitstagen pro Jahr.</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-wirkungsgrad">
    <dt>Wirkungsgrad und 80 PLUS <span class="en">(Efficiency Factor, 80 PLUS Certification)</span></dt>
    <dd><span class="label">Theorie</span><p>Der Wirkungsgrad eta ist das Verhältnis von abgegebener Nutzleistung P_ab zu aufgenommener Wirkleistung P_auf: eta = P_ab / P_auf (stets kleiner als 1 bzw. 100 %).<sup class="q"><a href="#a5-q4" title="80 PLUS Programm">4</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Die nicht nutzbare Leistung wird als Abwärme freigesetzt; Netzteile mit 80-PLUS-Zertifizierung (Bronze, Silber, Gold, Platin, Titan) garantieren mindestens 80 % Wirkungsgrad bei 20 %, 50 % und 100 % Last.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>Aufgenommene Leistung aus der Steckdose ist immer höher als die an die Komponenten abgegebene Leistung: P_auf = P_ab / eta.</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Berechnung der tatsächlich aus dem Stromnetz aufgenommenen Leistung anhand der internen Hardware-Verbrauchswerte und des Wirkungsgrads.</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-netzteil">
    <dt>Netzteilauslegung und Reserve <span class="en">(Power Supply Sizing, Safety Margin)</span></dt>
    <dd><span class="label">Theorie</span><p>Die Bemessung der Nennleistung eines Netzteils basierend auf der Summe der Maximallasten aller verbauten Hardwarekomponenten zuzüglich einer Sicherheits- und Auslastungsreserve.<sup class="q"><a href="#a5-q6" title="IHK-Konvention">6</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Ein Netzteil arbeitet bei ca. 50 % Auslastung am effizientesten; eine Reserve von 10 % bis 20 % fängt Einschaltströme und künftige Aufrüstungen ab.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>Sicherheitsreserve aufschlagen (z. B. Summe * 1,10) und auf die nächste handelsübliche Netzteilgröße (z. B. 450 W, 500 W, 550 W) aufrunden.</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Tabelle mit Komponentenverbräuchen summieren, prozentualen Aufschlag berechnen und eine marktübliche Nennleistung begründet auswählen.</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-amortisation">
    <dt>Amortisationsdauer <span class="en">(Payback Period)</span></dt>
    <dd><span class="label">Theorie</span><p>Der Zeitraum, nach dem die kumulierten jährlichen Kosteneinsparungen die zusätzlichen Anschaffungskosten einer energieeffizienteren Lösung vollständig ausgeglichen haben: Amortisation = Mehrpreis / jährliche Einsparung.<sup class="q"><a href="#a5-q1" title="Hering Physik">1</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Wirtschaftliche Entscheidungsgrundlage: Lohnt sich der Aufpreis für ein teureres 80-PLUS-Platin-Netzteil gegenüber einem Standard-Netzteil?</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>Einheit beachten: Mehrpreis in Euro geteilt durch Einsparung in Euro pro Jahr ergibt die Dauer in Jahren.</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Differenz der Anschaffungskosten durch die Differenz der jährlichen Stromkosten dividieren und auf Monate umrechnen.</p></dd>
  </dl>

  <dl class="begriff" id="a5-begriff-usv">
    <dt>Unterbrechungsfreie Stromversorgung (USV) <span class="en">(Uninterruptible Power Supply, UPS)</span></dt>
    <dd><span class="label">Theorie</span><p>Ein Gerät mit integrierten Akkumulatoren nach IEC 62040-3, das IT-Systeme bei Netzausfällen und Spannungsschwankungen für eine definierte Überbrückungszeit mit Strom versorgt.<sup class="q"><a href="#a5-q5" title="IEC 62040-3">5</a></sup></p></dd>
    <dd><span class="label">Praxis</span><p>Ermöglicht bei Stromausfall das kontrollierte Herunterfahren von Servern oder die Weiterarbeit bis zum Anspringen eines Notstromaggregats.</p></dd>
    <dd><span class="label">Merkhilfe und Verwechslung</span><p>USV-Klassen: VFD (Offline/Standby), VI (Line-Interactive), VFI (Online/Doppelwandler mit unterbrechungsfreier Umschaltzeit 0 ms).</p></dd>
    <dd><span class="label">In der Prüfung</span><p>Klassifizierung von USV-Arten oder grobe Abschätzung der Autonomiezeit (Batteriekapazität geteilt durch Last).</p></dd>
  </dl>

</section>

<section id="a5-kern">
  <h3>Das Verfahren</h3>

  <p>Die elektrotechnischen Berechnungen in der AP1 gliedern sich in drei grundlegende Verfahrensschritte: Leistungsbestimmung, Energie- und Kostenberechnung sowie die Auslegung von Stromversorgungskomponenten.<sup class="q"><a href="#a5-q1" title="Hering Physik">1</a></sup></p>

  <h4>1. Elektrische Grundgrößen im Formeldreieck</h4>
  <p>Für Gleichstrom und ohmsche Wechselstromverbraucher stehen Leistung, Spannung und Stromstärke in direkter Proportionalität zueinander:</p>

  <figure class="abb">
    <svg viewBox="0 0 640 180" role="img" aria-labelledby="a5-abb1-t">
      <title id="a5-abb1-t">Formeldreieck für elektrische Leistung P = U * I</title>
      <polygon class="f" points="320,20 200,160 440,160"/>
      <line class="a" x1="260" y1="90" x2="380" y2="90"/>
      <line class="a" x1="320" y1="90" x2="320" y2="160"/>
      
      <text class="mitte tb ta" x="320" y="65">P (Watt)</text>
      <text class="mitte tb" x="270" y="135">U (Volt)</text>
      <text class="mitte tb" x="370" y="135">I (Ampere)</text>
      
      <text class="klein" x="60" y="60">P = U * I  (Leistung)</text>
      <text class="klein" x="60" y="100">U = P / I  (Spannung)</text>
      <text class="klein" x="60" y="140">I = P / U  (Stromstärke)</text>
      
      <text class="klein" x="480" y="70">1 W = 1 V * 1 A</text>
      <text class="klein" x="480" y="110">1 kW = 1.000 W</text>
      <text class="klein" x="480" y="150">Netz: 230 V AC</text>
    </svg>
    <figcaption>Abb. A5-1: Das klassische Formeldreieck zur gegenseitigen Umrechnung von Leistung, Spannung und Stromstärke.</figcaption>
  </figure>

  <h4>2. Rechenkette zur Jahresstromkostenermittlung</h4>
  <p>Die Ermittlung der Betriebskosten erfolgt über eine geschlossene Rechenkette von der Leistungsaufnahme bis zum Rechnungsbetrag:</p>

  <figure class="abb">
    <svg viewBox="0 0 640 170" role="img" aria-labelledby="a5-abb2-t">
      <title id="a5-abb2-t">Rechenkette vom Geräteverbrauch zu den jährlichen Stromkosten</title>
      <rect class="w" x="20" y="50" width="125" height="50"/>
      <text class="mitte tb" x="82" y="72">Leistung</text>
      <text class="mitte klein t2" x="82" y="88">in Watt (W)</text>
      
      <line class="a" x1="145" y1="75" x2="180" y2="75" marker-end="url(#pfeil-a)"/>
      <text class="ta klein mitte" x="162" y="65">: 1.000</text>
      
      <rect class="f" x="180" y="50" width="125" height="50"/>
      <text class="mitte tb" x="242" y="72">Leistung</text>
      <text class="mitte klein t2" x="242" y="88">in kW</text>
      
      <line class="a" x1="305" y1="75" x2="340" y2="75" marker-end="url(#pfeil-a)"/>
      <text class="ta klein mitte" x="322" y="65">* Zeit</text>
      
      <rect class="f" x="340" y="50" width="130" height="50"/>
      <text class="mitte tb" x="405" y="72">Energie E</text>
      <text class="mitte klein t2" x="405" y="88">in kWh / Jahr</text>
      
      <line class="a" x1="470" y1="75" x2="505" y2="75" marker-end="url(#pfeil-a)"/>
      <text class="ta klein mitte" x="487" y="65">* EUR/kWh</text>
      
      <rect class="w" x="505" y="50" width="115" height="50"/>
      <text class="mitte tb" x="562" y="72">Kosten</text>
      <text class="mitte klein t2" x="562" y="88">in EUR / Jahr</text>
    </svg>
    <figcaption>Abb. A5-2: Von der Leistungsaufnahme in Watt über Betriebsstunden und Arbeitspreis zu den Jahreskosten.</figcaption>
  </figure>

  <h4>3. Wirkungsgrad und Energieverlust im Netzteil</h4>
  <p>Ein Netzteil wandelt Wechselspannung (230 V) in geregelte Gleichspannungen (+12 V, +5 V, +3,3 V) für die elektronischen Bauteile um. Der Wirkungsgrad bestimmt, wie viel Netzenergie als Abwärme verloren geht:</p>

  <figure class="abb">
    <svg viewBox="0 0 640 180" role="img" aria-labelledby="a5-abb3-t">
      <title id="a5-abb3-t">Leistungsfluss und Wirkungsgrad im PC-Netzteil</title>
      <rect class="w" x="30" y="65" width="140" height="50"/>
      <text class="mitte tb" x="100" y="87">P_auf (Netz)</text>
      <text class="mitte klein t2" x="100" y="103">500 W (100 %)</text>
      
      <line class="a" x1="170" y1="90" x2="240" y2="90" marker-end="url(#pfeil-a)"/>
      
      <rect class="f" x="240" y="45" width="160" height="90"/>
      <text class="mitte tb" x="320" y="80">Schaltnetzteil</text>
      <text class="mitte klein ta" x="320" y="100">Wirkungsgrad eta = 85 %</text>
      
      <line class="a" x1="400" y1="90" x2="470" y2="90" marker-end="url(#pfeil-a)"/>
      
      <rect class="w" x="470" y="65" width="140" height="50"/>
      <text class="mitte tb" x="540" y="87">P_ab (Hardware)</text>
      <text class="mitte klein t2" x="540" y="103">425 W (85 %)</text>
      
      <line class="d" x1="320" y1="135" x2="320" y2="165" marker-end="url(#pfeil)"/>
      <text class="klein rechts" x="430" y="155">Verlustleistung (Wärme): 75 W (15 %)</text>
    </svg>
    <figcaption>Abb. A5-3: Bei 85 % Wirkungsgrad werden von 500 W Aufnahmeleistung 425 W an die Hardware abgegeben und 75 W als Wärme frei.</figcaption>
  </figure>

  <h4>Rechenweg-Schema</h4>
<pre class="rechenweg">Gegeben: PC-Arbeitsplatz mit 160 W Leistungsaufnahme im Betrieb, 5 W im Standby.
Betriebszeiten: 220 Arbeitstage/Jahr, 8 Stunden Betrieb/Tag, 16 Stunden Standby/Tag.
Strompreis: 0,35 EUR / kWh.

1. Jahresverbrauch Betrieb:
   E_betrieb = (160 W / 1.000) * 8 h/Tag * 220 Tage/Jahr
   E_betrieb = 0,160 kW * 1.760 h = 281,60 kWh

2. Jahresverbrauch Standby:
   E_standby = (5 W / 1.000) * 16 h/Tag * 220 Tage/Jahr
   E_standby = 0,005 kW * 3.520 h = 17,60 kWh

3. Gesamter Energieverbrauch pro Jahr:
   E_gesamt  = 281,60 kWh + 17,60 kWh = 299,20 kWh

4. Jährliche Stromkosten:
   Kosten    = 299,20 kWh * 0,35 EUR/kWh = 104,72 EUR</pre>

  <h4>4. Netzteildimensionierung nach IHK-Konvention</h4>
  <p>Die Auslegung eines Netzteils folgt dem IHK-Berechnungsschema<sup class="q"><a href="#a5-q6" title="IHK-Konvention">6</a></sup>:</p>
  <ol>
    <li>Maximalverbräuche aller internen Komponenten (CPU, GPU, Mainboard, RAM, SSDs, Lüfter) summieren.</li>
    <li>Geforderten Sicherheitsaufschlag hinzurechnen (z. B. 10 % oder 20 % Reserve).</li>
    <li>Auf die nächsthöhere marktübliche Standard-Nennleistung aufrunden (Handelsstufen: 300 W, 350 W, 400 W, 450 W, 500 W, 550 W, 650 W, 750 W, 850 W).</li>
  </ol>

  <div class="merke" data-art="Typischer Fehler">
    <p>Vergessene Umrechnung von Watt in Kilowatt: Wer 160 W mit 1.760 Stunden multipliziert und das Ergebnis direkt mit dem kWh-Preis verrechnet, erhält um den Faktor 1.000 überhöhte Stromkosten (z. B. 98.560 EUR statt 98,56 EUR). Die Division durch 1.000 ist Pflicht.</p>
  </div>

  <div class="merke" data-art="Prüfungsnotiz">
    <p>USV-Dimensionierung: Bei Wechselstromnetzen wird zwischen Scheinleistung S in Voltampere (VA) und Wirkleistung P in Watt (W) unterschieden. Der Leistungsfaktor cos phi liegt bei PC-Netzteilen meist zwischen 0,7 und 0,9: P = S * cos phi.</p>
  </div>

</section>

<section id="a5-original">
  <h3>So hat die IHK gefragt</h3>

  <article class="aufgabe" id="a5-original-1">
    <p class="herkunft">AP1 Herbst 2025, Aufgabe 3.5, 2 Punkte, sinngemäß wiedergegeben<sup class="q"><a href="#a5-q7" title="AP1 Herbst 2025">7</a></sup></p>
    <div class="text">
      <p>Ein Kassenarbeitsplatz besteht aus einem PC-Terminal, einem Belegdrucker und einem Barcodescanner. An der 230-V-Netzsteckdose wird im aktiven Betrieb eine Gesamtaufnahme von 184 Watt gemessen.</p>
      <p>Berechnen Sie die Stromstärke I in Ampere, die dieser Kassenarbeitsplatz aus dem 230-V-Stromnetz aufnimmt.</p>
    </div>
    <details>
      <summary>Lösung mit Punktelogik</summary>
      <div class="inhalt">
        <p><strong>Rechenweg:</strong></p>
        <ol>
          <li>Formel: P = U * I  →  I = P / U</li>
          <li>Zahlenansatz: I = 184 W / 230 V</li>
          <li>Ergebnis: I = 0,80 A (Ampere)</li>
        </ol>
        <p><strong>Punkteverteilung:</strong> 1 Punkt für den korrekten Formelansatz, 1 Punkt für das richtige Ergebnis mit Einheit Ampere (insgesamt 2 Punkte).</p>
      </div>
    </details>
  </article>

  <article class="aufgabe" id="a5-original-2">
    <p class="herkunft">AP1 Frühjahr 2024, Aufgabe 3.7, 4 Punkte, sinngemäß wiedergegeben<sup class="q"><a href="#a5-q8" title="AP1 Frühjahr 2024">8</a></sup></p>
    <div class="text">
      <p>Für eine neue Grafik-Workstation werden folgende maximale Komponentenleistungen ermittelt:</p>
      <ul>
        <li>Prozessor (CPU): 125 Watt</li>
        <li>Grafikkarte (GPU): 220 Watt</li>
        <li>Mainboard, Arbeitsspeicher und Lüfter: 45 Watt</li>
        <li>Zwei NVMe-SSDs: zusammen 18 Watt</li>
      </ul>
      <p>Zur Vermeidung von Überlastungen und für spätere Erweiterungen ist eine Sicherheitsreserve von 15 Prozent auf die Gesamtsumme aufzuschlagen. Bestimmen Sie die Mindestleistung des Netzteils und wählen Sie die passende Standard-Nennleistung aus der Reihe 400 W, 450 W, 500 W, 550 W, 650 W, 750 W begründet aus.</p>
    </div>
    <details>
      <summary>Lösung mit Punktelogik</summary>
      <div class="inhalt">
        <p><strong>Rechenweg:</strong></p>
        <ol>
          <li>Summe der Komponenten: 125 W + 220 W + 45 W + 18 W = 408 Watt.</li>
          <li>Sicherheitsreserve (15 % Aufschlag): 408 W * 1,15 = 469,20 Watt.</li>
          <li>Auswahl der Nennleistung: Die Mindestleistung von 469,2 W liegt über der 450-W-Stufe. Das nächstgrößere Netzteil aus der Reihe ist die <strong>500-W-Stufe</strong> (oder alternativ 550 W bei großzügiger Auslegung).</li>
        </ol>
        <p><strong>Punkteverteilung:</strong> 1 Punkt für Komponentensumme (408 W), 1 Punkt für Sicherheitsaufschlag (469,2 W), 2 Punkte für Auswahl und nachvollziehbare Begründung des 500-W- oder 550-W-Netzteils (insgesamt 4 Punkte).</p>
      </div>
    </details>
  </article>

</section>

<section id="a5-variante">
  <h3>Jetzt du</h3>

  <article class="aufgabe" id="a5-variante-1">
    <p class="herkunft">Variante zu Aufgabe 3.5 (Herbst 2025)</p>
    <div class="text">
      <p>An einem Serverrack mit vier 1HE-Servern wird eine Gesamtstromaufnahme von 4,6 A bei einer Versorgungsspannung von 230 V gemessen.</p>
      <p>Berechnen Sie die aufgenommene Gesamtleistung P in Watt und Kilowatt.</p>
    </div>
    <details>
      <summary>Lösung</summary>
      <div class="inhalt">
        <p><strong>Lösungsweg:</strong></p>
        <ol>
          <li>Formel: P = U * I</li>
          <li>Zahlenansatz: P = 230 V * 4,6 A = 1.058 Watt</li>
          <li>In Kilowatt: 1.058 W / 1.000 = 1,058 kW</li>
        </ol>
      </div>
    </details>
  </article>

  <article class="aufgabe" id="a5-variante-2">
    <p class="herkunft">Variante zu Aufgabe 3.7 (Frühjahr 2024)</p>
    <div class="text">
      <p>Ein Entwicklungs-PC soll mit einem neuen Netzteil ausgestattet werden. Die Komponenten haben folgende Spitzenverbräuche: CPU 105 W, GPU 160 W, Mainboard und RAM 35 W, zwei SSDs 14 W. Die Firmenrichtlinie verlangt eine Sicherheitsreserve von 20 Prozent.</p>
      <p>Berechnen Sie die berechnete Mindestleistung und wählen Sie das passende Netzteil aus der Reihe (350 W, 400 W, 450 W, 500 W) aus.</p>
    </div>
    <details>
      <summary>Lösung</summary>
      <div class="inhalt">
        <p><strong>Lösungsweg:</strong></p>
        <ol>
          <li>Komponentensumme: 105 W + 160 W + 35 W + 14 W = 314 Watt.</li>
          <li>Sicherheitsreserve (20 %): 314 W * 1,20 = 376,80 Watt.</li>
          <li>Auswahl: 376,8 W übersteigt 350 W. Gewählt wird das <strong>400-W-Netzteil</strong>.</li>
        </ol>
      </div>
    </details>
  </article>

</section>

<section id="a5-selbstcheck">
  <h3>Selbstcheck</h3>
  <ol class="selbstcheck">
    <li>Ein Büro-PC nimmt im Betrieb 90 Watt auf und läuft an 250 Tagen im Jahr für jeweils 8 Stunden. Wie hoch ist der jährliche Energieverbrauch in Kilowattstunden?
      <details><summary>Antwort</summary><div class="inhalt"><p>Rechnung: (90 W / 1.000) * 8 Stunden/Tag * 250 Tage = 0,090 kW * 2.000 h = 180 kWh pro Jahr.</p></div></details>
    </li>
    <li>Was bedeutet die Zertifizierung 80 PLUS Gold für ein PC-Schaltnetzteil?
      <details><summary>Antwort</summary><div class="inhalt"><p>Sie bescheinigt, dass das Netzteil bei 230 V Netzspannung einen Wirkungsgrad von mindestens 90 % bei 20 % Last, mindestens 92 % bei 50 % Last und mindestens 89 % bei Volllast (100 %) erzielt. Entsprechend gering ist die in Abwärme umgewandelte Verlustleistung.</p></div></details>
    </li>
    <li>Worin liegt der wesentliche Unterschied zwischen einer VFD-USV (Offline) und einer VFI-USV (Online / Doppelwandler)?
      <details><summary>Antwort</summary><div class="inhalt"><p>Die VFD-USV leitet den Netzstrom im Normalbetrieb direkt durch und schaltet bei Netzausfall mit einer kurzen Verzögerung (meist 4 bis 10 ms) auf Akkubetrieb um. Die VFI-USV wandelt den Wechselstrom permanent in Gleichstrom und wieder in Wechselstrom um (Doppelwandler); sie hat eine Umschaltzeit von exakt 0 ms und filtert alle Netzstörungen vollständig heraus.</p></div></details>
    </li>
  </ol>
</section>

<section id="a5-quellen">
  <h3>Quellen dieses Kapitels</h3>
  <ol class="quellenliste">
    <li id="a5-q1" data-src="hering-physik"><span class="typ">Fachbuch</span> Hering, E.; Martin, R.; Stohrer, M.: Physik für Ingenieure, 12. Aufl., Springer Vieweg, Berlin/Heidelberg 2016, Kapitel Elektrizitätslehre. <span class="abruf">(nicht online geprüft)</span></li>
    <li id="a5-q2" data-src="europa-tabellenbuch-it"><span class="typ">Fachbuch</span> Biehler, B. et al.: IT-Handbuch IT-Systemelektroniker/-in, Fachinformatiker/-in, 11. Aufl., Europa-Lehrmittel, Haan-Gruiten 2021, Grundlagen der Elektrotechnik. <span class="abruf">(nicht online geprüft)</span></li>
    <li id="a5-q3" data-src="bnetza-monitoring"><span class="typ">Behörde</span> Bundesnetzagentur; Bundeskartellamt: Monitoringbericht Energie, Bonn. <a href="https://www.bundesnetzagentur.de/DE/Fachthemen/ElektrizitaetundGas/Monitoringberichte/start.html">bundesnetzagentur.de Monitoringberichte</a> <span class="abruf">(abgerufen 2026-09-03)</span></li>
    <li id="a5-q4" data-src="clearesult-80plus"><span class="typ">Hersteller</span> CLEAResult: 80 PLUS Program – Power Supply Efficiency Verification, Portland. <a href="https://www.clearesult.com/80plus/">clearesult.com/80plus</a> <span class="abruf">(abgerufen 2026-09-03)</span></li>
    <li id="a5-q5" data-src="iec-62040-3"><span class="typ">Norm</span> International Electrotechnical Commission (IEC): IEC 62040-3:2021 – Uninterruptible power systems (UPS) – Part 3, Genf 2021. <span class="abruf">(nicht online geprüft)</span></li>
    <li id="a5-q6" data-src="ihk-konvention-strom"><span class="typ">IHK-Konvention</span> ZPA Nord-West: Lösungshinweise zu Stromkosten- und Netzteilberechnungen der AP1, Rechenschemata und Dimensionierungsregeln. <span class="abruf">(nicht online geprüft)</span></li>
    <li id="a5-q7" data-src="ihk-ap1-h2025"><span class="typ">IHK-Prüfung</span> ZPA Nord-West: Aufgabenheft und Lösungshinweise Abschlussprüfung Herbst 2025, Teil 1, Aufgabe 3.5. <span class="abruf">(nicht online geprüft)</span></li>
    <li id="a5-q8" data-src="ihk-ap1-f2024"><span class="typ">IHK-Prüfung</span> ZPA Nord-West: Aufgabenheft und Lösungshinweise Abschlussprüfung Frühjahr 2024, Teil 1, Aufgabe 3.7. <span class="abruf">(nicht online geprüft)</span></li>
  </ol>
</section>

</section>
'''

target_file = r"C:\Users\mu.aycetin\Desktop\Lernen\bau\kapitel\14-a5.html"
with open(target_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print("14-a5.html geschrieben, starte check.js...")
res = subprocess.run(["node", "bau/pruef/check.js", "bau/kapitel/14-a5.html", "--fragment"], cwd=r"c:\Users\mu.aycetin\Desktop\Lernen", capture_output=True, text=True)
print("STDOUT:\n", res.stdout)
print("STDERR:\n", res.stderr)
print("Exit-Code:", res.returncode)
