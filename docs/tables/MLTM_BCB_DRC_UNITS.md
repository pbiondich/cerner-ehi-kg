# MLTM_BCB_DRC_UNITS

> Storing valid Dose Units for BCB to perform Dose Range Checking

**Description:** Multum BCB Dose Range Checking Units  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BCB_UNIT` | VARCHAR(50) | NOT NULL |  | Identifies the corresponding BCB unit utilized by BCB Dose Range Checking |
| 2 | `GLOBAL_TXT` | VARCHAR(50) | NOT NULL |  | Global drug identifier |
| 3 | `GLOBAL_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the type of Global Identifier stored in a Global_Txt |
| 4 | `UNIT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the valid unit utilized by BCB Dose Range Checking |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GLOBAL_TYPE_ID` | [MLTM_GLOBAL_TYPE](MLTM_GLOBAL_TYPE.md) | `GLOBAL_TYPE_ID` |
| `UNIT_ID` | [MLTM_UNITS](MLTM_UNITS.md) | `UNIT_ID` |

