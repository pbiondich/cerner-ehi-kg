# RAD_RES_INFO

> The Rad_Res_Info table contains information about a physican or resident specific to radiology.

**Description:** Radiologist Resident Information  
**Table type:** REFERENCE  
**Primary key:** `PERSON_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLOW_TO_PROXY_IND` | DOUBLE |  |  | The Allow_To_Proxy_Ind indicates if others are allowed to proxy reports for this radiologist/resident. |
| 2 | `ASSIGNED_RAD_ID` | DOUBLE | NOT NULL | FK→ | This column contains the id of the radiologist associated with the specified resident. |
| 3 | `PASSWORD` | VARCHAR(20) |  |  | This field is currently not used. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | PK FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `PREVENT_PUBLISH_PRELIM_IND` | DOUBLE | NOT NULL |  | Indicates if resident is prevented from publishing preliminary reports. |
| 6 | `PROXY_ALLOWED_IND` | DOUBLE |  |  | The Proxy_Allowed_Ind indicates if this specific radiologist/resident is allowed to proxy at all. |
| 7 | `QUE_LOCK_DT_TM` | DATETIME |  |  | This is the date and time that the queue was last accessed. |
| 8 | `QUE_LOCK_ID` | DOUBLE | NOT NULL | FK→ | This is the id of the current lock holder of this queue. |
| 9 | `REQUIRE_PASS_IND` | DOUBLE |  |  | If this indicator is true, then the system will re-prompt the user for a password when cases are submitted in case signout. |
| 10 | `RES_SIGNOUT_IND` | DOUBLE |  |  | This column indicates if a resident is able to finalize reports. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSIGNED_RAD_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `QUE_LOCK_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PROXY_EXEMPTIONS](PROXY_EXEMPTIONS.md) | `PERSON_ID` |
| [PROXY_GROUP](PROXY_GROUP.md) | `PERSON_ID` |
| [RES_SIGN_ACT_SUBTYPE](RES_SIGN_ACT_SUBTYPE.md) | `PERSON_ID` |

