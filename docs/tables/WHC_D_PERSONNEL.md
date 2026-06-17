# WHC_D_PERSONNEL

> WHC Reporting - Dimension Table identifying all PERSONNEL involved in treatment of the Mother and Child during Pregnancy and Delivery.

**Description:** WHC_D_PERSONNEL  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_PERSONNEL_ID`  
**Columns:** 8  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MILL_PERSON_ID` | DOUBLE |  |  | Foreign key to PRSNL.PERSON_ID, representing the corresponding member of personnel in Millennium. |
| 2 | `PRSNL_NAME` | VARCHAR(255) |  |  | Personnel name |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 8 | `WHC_D_PERSONNEL_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (12)

| From table | Column |
|------------|--------|
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `ATTENDING_PHYSICIAN_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `ANESTHESIOLOGIST_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `ANESTHETIST_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `ASST_PHYSICIAN_1_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `ASST_PHYSICIAN_2_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_CNM_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_PEDIATRICIAN_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_PHYSICIAN_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_RN_1_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `DELIVERY_RN_2_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `RESUS_RN_1_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `SCRUB_TECHNICIAN_ID` |

