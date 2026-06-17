# OEN_SCRIPT

> open engine script Table

**Description:** open engine script  
**Table type:** REFERENCE  
**Primary key:** `SCRIPT_NAME`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BUILD_DATE` | CHAR(10) |  |  | Future: Date when script was compiled |
| 2 | `BUILD_TIME` | CHAR(8) |  |  | Future: the time the script was compiled. |
| 3 | `NOT_EXECUTABLE` | DOUBLE |  |  | A flag which determines if script is executable by user or not. |
| 4 | `READ_ONLY` | DOUBLE |  |  | A flag which determines if a script is read only or not. |
| 5 | `SCRIPT_BODY` | LONGTEXT |  |  | Actual script body |
| 6 | `SCRIPT_DESC` | VARCHAR(80) |  |  | script descriptionColumn |
| 7 | `SCRIPT_LANGUAGE` | VARCHAR(20) |  |  | The scripting language that the script was written in. An empty/null value indicates the scripting language is CCL for passivity. |
| 8 | `SCRIPT_NAME` | CHAR(32) | NOT NULL | PK | Script name - Unique identifier |
| 9 | `SCRIPT_REFCNT` | DOUBLE |  |  | Passed to a user to determine if some one else has not updated a script before him/her. |
| 10 | `SCRIPT_TYPE` | CHAR(20) |  |  | script typeColumn |
| 11 | `UPDT_DATE` | CHAR(10) |  |  | A date when script was created or last updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TIME` | CHAR(8) |  |  | A time when script was created or last updated. |
| 14 | `USER_NAME` | CHAR(32) |  |  | User name who created or updated the script. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OEN_SCRIPT_HIST](OEN_SCRIPT_HIST.md) | `SCRIPT_NAME` |

