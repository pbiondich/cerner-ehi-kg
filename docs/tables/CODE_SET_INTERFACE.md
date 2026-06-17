# CODE_SET_INTERFACE

> This table is used by ESI and ESO to define code value alias processing rules.

**Description:** Code Set Interface Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ALIAS_TYPE_MEANING` | VARCHAR(12) |  |  | The meaning of the alias. Used when alias is not unique enough within a code_set. |
| 3 | `CODE_SET` | DOUBLE | NOT NULL | FK→ | The number of the code set header record (determined by following the procedure for creating a new code set). |
| 4 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 5 | `DEFAULT_ALIAS` | VARCHAR(255) |  |  | This may define the default alias string to use (maining for ESO) when an outbound alias can not be found for a code value. |
| 6 | `DEFAULT_CD` | DOUBLE | NOT NULL |  | This may define the default code value to use when an inbound alias is not found for a particular code set. |
| 7 | `PROCESS_CD` | DOUBLE | NOT NULL |  | The field defines the processing meaning/function when the alias for code value by either the ESI or ESO servers. |
| 8 | `SYS_DIRECTION_CD` | DOUBLE | NOT NULL |  | This define the direction of the interface either TO_HNA or FROM_HNA. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CODE_SET` | [CODE_VALUE_SET](CODE_VALUE_SET.md) | `CODE_SET` |

