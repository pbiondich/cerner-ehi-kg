# WHC_D_EPISIOTOMY

> WHC Reporting - Dimension Table identifying Episiotomy information at time of delivery

**Description:** WHC_D_EPISIOTOMY  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_EPISIOTOMY_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EPISIOTOMY_DEGREE` | VARCHAR(255) |  |  | User-readable description of 'Epistiotomy degree' value, taken from clinical result recorded against CKI CERNER!93130FE6-0444-4DE2-90C4-DE2CD6A00493/CERNER!919A00D1-41C2-4717-99E5-1D7147DF69A8(free-text). |
| 2 | `EPISIOTOMY_LOCATION` | VARCHAR(255) |  |  | User-readable description of 'Episiotomy location' value, taken from clinical result recorded against CKI CERNER!9BA38221-D628-4E4B-9D8F-BF7FA6DA0E6F. |
| 3 | `MILL_EPI_DEGREE_NOMEN_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Episiotomy degree' value in Millennium. |
| 4 | `MILL_EPI_LOCATION_NOMEN_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Episiotomy location' value in Millennium. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 10 | `WHC_D_EPISIOTOMY_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `EPISIOTOMY_ID` |

