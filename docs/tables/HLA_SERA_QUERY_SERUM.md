# HLA_SERA_QUERY_SERUM

> Defines a specific sera which belongs to a query. The data containted is a snapshot view of when the data was created.

**Description:** HLA Sera Query Serum  
**Table type:** ACTIVITY  
**Primary key:** `SERA_QUERY_SERUM_ID`  
**Columns:** 29  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABORH` | CHAR(80) |  |  | The ABO/Rh blood type. This field is a snapshot of the code value's display when the record was saved. |
| 2 | `ACCESSION` | CHAR(20) |  |  | The unformatted accession number. |
| 3 | `ANTIBODIES` | VARCHAR(100) |  |  | The list of antibodies. This field is a snapshot of the list of antibody's code value display when the record was saved. |
| 4 | `FMT_ACCESSION` | CHAR(40) |  |  | The formatted accession. This field is a snapshot of the formatted accession when the record was saved. |
| 5 | `HIC` | VARCHAR(200) |  |  | The HIC alias replaces the UNOS alias. All previous UNOS aliases should display as the HIC alias. A README will be required to copy data from the UNOS column to the HIC column. Going forward, only the HIC column will be populated. |
| 6 | `HLA_AB_SCREEN_ID` | DOUBLE | NOT NULL | FK→ | Identifies the manual record to which this serum belongs. It is a foreign key reference to the primary key of the person_hla_ab_screen table. |
| 7 | `LOCATION` | VARCHAR(255) |  |  | The location. This field is a snapshot of the code value's display when the record was saved. |
| 8 | `MRN` | VARCHAR(200) |  |  | The medical record number. This field is a snapshot of the MRN when the record was saved. |
| 9 | `NAME_FULL_FORMATTED` | VARCHAR(100) |  |  | The name full formatted. This field is a snapshot of the person's name full formatted when the record was saved. |
| 10 | `NMDP` | VARCHAR(200) |  |  | The NMDP number. This field is a snapshot of the NMDP when the record was saved. The NMDP is pulled from the person alias type codeset. |
| 11 | `OPO` | VARCHAR(200) |  |  | OPO Alias for OPO Donor ID / OPO Recipient ID |
| 12 | `ORDER_DT_TM` | DATETIME |  |  | The order date and time for the serum. |
| 13 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifies the non-manual record to which this serum belongs. It is a foreign key reference to the primary key of the orders table. |
| 14 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | The order mnemonic. This field is a snapshot of the order mnemonic when the record was saved. |
| 15 | `ORDER_STATUS` | CHAR(40) |  |  | The order status. This field is a snapshot of the code value's display when the record was saved. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `POSSIBLE_AB_STRING` | VARCHAR(255) |  |  | The list of possible antibodies. This field is a snapshot of the string of possible antibodies when the record was saved. |
| 18 | `RECIPIENT_STATUS` | VARCHAR(255) |  |  | The recipient status. This field is a snapshot of the code value's display when the record was saved. |
| 19 | `REMOVED_IND` | DOUBLE |  |  | Variable to indicate whether the serum should be displayed in the retrieved or removed spreadsheet. |
| 20 | `SERA_QUERY_ID` | DOUBLE | NOT NULL | FK→ | Identifies the sera query record to which this query belongs. It is a foreign key reference to the primary key of the hla_sera_query table. |
| 21 | `SERA_QUERY_SERUM_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a Sera Query Serum record. |
| 22 | `SERUM_QUERY_INFO` | VARCHAR(255) |  |  | Textual information pertaining to the record's serum. |
| 23 | `TRANSPLANT_CENTER` | VARCHAR(255) |  |  | The transplant center. This field is a snapshot of the code value's display when the record was saved. |
| 24 | `UNOS` | VARCHAR(200) |  |  | The UNOS number. This field is a snapshot of the UNOS when the record was saved. The UNOS is pulled from the person alias type codeset. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HLA_AB_SCREEN_ID` | [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `HLA_AB_SCREEN_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `SERA_QUERY_ID` | [HLA_SERA_QUERY](HLA_SERA_QUERY.md) | `SERA_QUERY_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_SERA_QUERY_AB](HLA_SERA_QUERY_AB.md) | `SERA_QUERY_SERUM_ID` |
| [HLA_SERA_QUERY_R](HLA_SERA_QUERY_R.md) | `SERA_QUERY_SERUM_ID` |

