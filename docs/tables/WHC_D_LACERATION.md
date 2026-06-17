# WHC_D_LACERATION

> WHC Reporting - Dimension Table identifying Laceration information at time of delivery

**Description:** WHC_D_LACERATION  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_LACERATION_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LACERATION_DEGREE` | VARCHAR(255) |  |  | User-readable description of 'Laceration degree' value, taken from clinical result recorded against CKI CERNER!AF0246A9-BE66-4EB2-978F-C2090B8AAE2F. |
| 2 | `LACERATION_LOCATION` | VARCHAR(255) |  |  | User-readable description of 'Laceration location' value, taken from clinical result recorded against CKI CERNER!EC433F99-663D-4A9C-92F2-09D6AB766188. |
| 3 | `LACERATION_REPAIR` | VARCHAR(255) |  |  | User-readable description of 'Laceration repair' value, taken from clinical result recorded against CKI CERNER!7A835932-1863-408C-A379-FAFCB64788C3. |
| 4 | `MILL_LAC_DEGREE_NOMEN_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Laceration degree' value in Millennium. |
| 5 | `MILL_LAC_LOCATION_NOMEN_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Laceration location' value in Millennium. |
| 6 | `MILL_LAC_REPAIR_NOMEN_ID` | DOUBLE |  |  | Foreign key to NOMENCLATURE.NOMENCLATURE_ID, represeting the corresponding 'Laceration repair' value in Millennium. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WHC_D_LACERATION_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `LACERATION_ID` |

