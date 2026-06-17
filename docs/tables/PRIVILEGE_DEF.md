# PRIVILEGE_DEF

> This table defines the template for each definition.

**Description:** Privilege Definition  
**Table type:** REFERENCE  
**Primary key:** `PRIVILEGE_DEF_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_GRANTED_IND` | DOUBLE | NOT NULL |  | Indicates whether the default value is granted for this privilege if no activity privilege or legacy privilege values are set. |
| 2 | `EXCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set to "yes, except for" (exclude). |
| 3 | `INCLUDE_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set to "no, except for" (include). |
| 4 | `LOCATION_PERSON_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a person at a specific location. |
| 5 | `LOCATION_POSITION_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a position at a specific location. |
| 6 | `LOCATION_PPR_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a person patient relationship at a specific location. |
| 7 | `NO_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set to"no" (denied). |
| 8 | `PERSON_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a person. |
| 9 | `POSITION_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a position. |
| 10 | `PPR_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set for a person patient relationship. |
| 11 | `PRIVILEGE_CD` | DOUBLE | NOT NULL | FK→ | Privilege code of the privilege that is being defined . |
| 12 | `PRIVILEGE_DEF_ID` | DOUBLE | NOT NULL | PK | Primary key for the privilege definition table. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 18 | `YES_IND` | DOUBLE | NOT NULL |  | Indicates whether this privilege can be set to "yes" (granted). |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRIVILEGE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRIVILEGE_EXCEPTION_DEF](PRIVILEGE_EXCEPTION_DEF.md) | `PRIVILEGE_DEF_ID` |

