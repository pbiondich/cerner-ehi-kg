# HLA_AB_SCRN_WELL_CELL

> Defines a unique identifier for a specific donor's cells used in building an HLA antibody screen or screens.

**Description:** HLA Antibody Screen Well Cell  
**Table type:** REFERENCE  
**Primary key:** `CELL_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CELL_COMMENT` | VARCHAR(255) |  |  | Comment pertaining to the cells contained in a well of an Antibody Screen. |
| 3 | `CELL_DESC` | VARCHAR(20) |  |  | The description of the cells contained in a well of an Antibody Screen. This is typically provided by the manufacturer of the screen or is named after the donor of the cells. Unique identifier the user gives the Antibody Screen well cell. |
| 4 | `CELL_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies an Antibody Screen well cell. |
| 5 | `CONTROL_IND` | DOUBLE |  |  | Indicates that antibody screen well contains a control instead of testing cells. This will exclude it from being used in PRA calculations. |
| 6 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | The code for the manufacturer who uses the well cells in making Antibody Screens |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [HLA_AB_SCRN_WELL](HLA_AB_SCRN_WELL.md) | `CELL_ID` |
| [WELL_CELL_ANTIGEN](WELL_CELL_ANTIGEN.md) | `CELL_ID` |

