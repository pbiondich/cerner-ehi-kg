# WELL_CELL_ANTIGEN

> Defines a single antigen which is present in a specific donor's cells used in building an HLA antibody screen or screens.

**Description:** Well Cell Antigen  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIGEN_CD` | DOUBLE | NOT NULL |  | The code for the antigen included in the HLA Antibody Screen well cell definition. |
| 2 | `ANTIGEN_SEQ` | DOUBLE | NOT NULL |  | Specifies the sequence of the antigen included in the HLA Antibody Screen well cell definition. |
| 3 | `CELL_ID` | DOUBLE | NOT NULL | FK→ | Identifies in conjunction with manufacturer the unique cells contained in an Antibody Screen tray well. Cell_id and manufacturer_cd are a foreign key reference to the primary key of the hla_ab_scrn_well_cell table. |
| 4 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | No longer used. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CELL_ID` | [HLA_AB_SCRN_WELL_CELL](HLA_AB_SCRN_WELL_CELL.md) | `CELL_ID` |

