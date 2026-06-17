# HLA_TRAY_WELL_SERUM

> Defines a unique identifier for a specific donor's serum used in building an HLA typing tray or trays.

**Description:** HLA Typing Tray Well Serum  
**Table type:** REFERENCE  
**Primary key:** `SERUM_ID`  
**Columns:** 10  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The code for the manufacturer who uses the well serum in making HLA Typing trays. |
| 3 | `SERUM_COMMENT` | VARCHAR(255) |  |  | Comment pertaining to the serum contained in a well of an HLA Typing tray. |
| 4 | `SERUM_DESC` | VARCHAR(20) |  |  | The description of the serum contained in a well of an HLA Typing tray. This is typically provided by the manufacturer of the tray or is named after the donor of the serum. Unique identifier the user gives the HLA Typing tray well serum. |
| 5 | `SERUM_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an HLA Typing tray well serum. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_TYP_TRAY_WELL](HLA_TYP_TRAY_WELL.md) | `SERUM_ID` |
| [WELL_SERUM_AB](WELL_SERUM_AB.md) | `SERUM_ID` |

