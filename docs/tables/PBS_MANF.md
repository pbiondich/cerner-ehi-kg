# PBS_MANF

> Australian Pharmaceutical Benefits Manufacturer data

**Description:** PBS_MANF  
**Table type:** REFERENCE  
**Primary key:** `PBS_MANUFACTURER_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACSIMILIE_NUMBER` | VARCHAR(16) | NOT NULL |  | Facsimile number ¿ numeric only |
| 2 | `MANUFACTURER_CODE` | VARCHAR(20) | NOT NULL |  | PBS XML manufacturer code |
| 3 | `MANUFACTURER_IDENT` | VARCHAR(8) | NOT NULL |  | Manufacturer XML Reference ID |
| 4 | `MANUFACTURER_NAME` | VARCHAR(99) | NOT NULL |  | Manufacturer name |
| 5 | `PBS_MANUFACTURER_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_MANF table. It is an internal system assigned number. |
| 6 | `STREET_ADDRESS` | VARCHAR(200) | NOT NULL |  | Street address |
| 7 | `TELEPHONE_NUMBER` | VARCHAR(16) | NOT NULL |  | Telephone number |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PBS_DRUG](PBS_DRUG.md) | `PBS_MANUFACTURER_ID` |

