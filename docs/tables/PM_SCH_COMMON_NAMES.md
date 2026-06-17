# PM_SCH_COMMON_NAMES

> This table is needed for a search quality project, it will store all name_keys with a count > 500 up to 32k. We will use this to let the user know if they are going to execute a search that will fail, before they click search.

**Description:** Person Management Schedule Common Names  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | Used for multi-tenet sites to stamp the logical domain id. |
| 2 | `NAME_CNT` | DOUBLE | NOT NULL |  | Number of names for that NAME_KEY & TYPE. |
| 3 | `NAME_KEY` | VARCHAR(255) | NOT NULL |  | This corresponds to the FIRST_NAME_KEY, LAST_NAME KEYS on the PERSON table, but they can also be combo of both. |
| 4 | `NAME_TYPE_CD` | DOUBLE | NOT NULL |  | Type code that designates between FIRST, LAST and COMBO types. |
| 5 | `PM_SCH_COMMON_NAMES_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the pm_sch_common_names |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |

