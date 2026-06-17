# PRSNL_ROLE_PROFILE

> Stores a personnel's role profile.

**Description:** Personnel Role Profile  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_ROLE_PROFILE_ID`  
**Columns:** 16  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CHART_ACCESS_PRSNL_GROUP_ID` | DOUBLE |  | FK→ | Uniquely identifies the chart access personnel group associated to the role profile. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `POSITION_CD` | DOUBLE | NOT NULL |  | The position code of the role profile. |
| 6 | `PREFERRED_ROLE_VALUE` | DOUBLE |  |  | This defines whether a role profile is preferred or not. (0 = Not Preferred, 1 = Preferred) |
| 7 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the personnel to which the role profile is associated . |
| 8 | `PRSNL_ROLE_PROFILE_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a row on the prsnl_role_profile table. |
| 9 | `ROLE_PROFILE_TEXT` | VARCHAR(200) |  |  | The display string of the role profile. |
| 10 | `ROLE_PROFILE_TEXT_KEY` | VARCHAR(200) | NOT NULL |  | This field contains the role_profile_text with all special characters removed and all alpha characters converted to uppercase. |
| 11 | `ROLE_PROFILE_TEXT_KEY_A_NLS` | VARCHAR(800) |  |  | Stores the corresponding non-english ACCENTED character set values for _KEY columns. Used for sorting non-english text. Database triggers handle the population of these columns so CCL scripts and applications can ignore them. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHART_ACCESS_PRSNL_GROUP_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PRSNL_ROLE_PROFILE_ATTR](PRSNL_ROLE_PROFILE_ATTR.md) | `PRSNL_ROLE_PROFILE_ID` |

