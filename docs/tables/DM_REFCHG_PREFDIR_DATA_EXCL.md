# DM_REFCHG_PREFDIR_DATA_EXCL

> Stores information used to exclude certain overrides in DM_REFCHG_PREFDIR_DATA from certain preferences.

**Description:** Database Architecture Refchg Prefdir Data Exclusions  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DIST_NAME_EXCLUDE` | VARCHAR(2000) | NOT NULL |  | Holds the exclusion string |
| 3 | `DM_REFCHG_PREFDIR_DATA_EXCL_ID` | DOUBLE | NOT NULL |  | Primary Key for table. Does not use a standard Oracle sequence - Controlled and shipped from in-house (exception_flg = 1) |
| 4 | `DM_REFCHG_PREFDIR_DATA_ID` | DOUBLE | NOT NULL | FK→ | Holds the reference back to the PK of the DM_REFCHG_PREFDIR_DATA Does not use a standard Oracle Sequence - Controlled and shipped from in-house (exception_flg = 1) |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DM_REFCHG_PREFDIR_DATA_ID` | [DM_REFCHG_PREFDIR_DATA](DM_REFCHG_PREFDIR_DATA.md) | `DM_REFCHG_PREFDIR_DATA_ID` |

