# WELL_SERUM_AB

> Defines a single antibody which is present in a specific donor's serum used in building an HLA typing tray or trays.

**Description:** Well Serum Antibody  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANTIBODY_CD` | DOUBLE | NOT NULL |  | The code for the antibody included in the HLA Typing tray well serum definition. |
| 2 | `ANTIBODY_SEQ` | DOUBLE | NOT NULL |  | Specifies the sequence of the antibody included in the HLA Typing tray well serum definition. |
| 3 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | No longer used. |
| 4 | `SERUM_ID` | DOUBLE | NOT NULL | FK→ | Identifies in conjunction with manufacturer the unique serum contained in an HLA Typing tray well. Serum_id and manufacturer_cd are a foreign key reference to the primary key of the hla_tray_well_serum table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SERUM_ID` | [HLA_TRAY_WELL_SERUM](HLA_TRAY_WELL_SERUM.md) | `SERUM_ID` |

