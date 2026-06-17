# PRSNL_ROLE_PROFILE_ATTR

> Stores personnel role profile attributes.

**Description:** Personnel Role Profile Attributes  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATTR_TEXT` | VARCHAR(255) | NOT NULL |  | A text value of the role profile attribute. |
| 2 | `ATTR_TEXT_KEY` | VARCHAR(255) | NOT NULL |  | The text value of the role profile attribute, in all capitals, spaces and special characters removed for better searchability. |
| 3 | `ATTR_TEXT_KEY_A_NLS` | VARCHAR(1020) |  |  | Stores the corresponding non-english ACCENTED character set values for _KEY columns. Used for sorting non-english text. Database triggers handle the population of these columns so CCL scripts and applications can ignore them. |
| 4 | `ATTR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of role profile attribute. |
| 5 | `PRSNL_ROLE_PROFILE_ATTR_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the prsnl_role_profile_attr table. |
| 6 | `PRSNL_ROLE_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the prsnl_role_profile table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ROLE_PROFILE_ID` | [PRSNL_ROLE_PROFILE](PRSNL_ROLE_PROFILE.md) | `PRSNL_ROLE_PROFILE_ID` |

