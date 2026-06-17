# PERSON_MATCH_REV

> PERSON MATCH REV

**Description:** PERSON MATCH REV desc  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 51

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `A_ALIAS1` | VARCHAR(200) |  |  | This is the first alias. |
| 6 | `A_ALIAS2` | VARCHAR(200) |  |  | This is the second alias. |
| 7 | `A_ALIAS3` | VARCHAR(200) |  |  | This is the third alias. |
| 8 | `A_ALIAS_POOL1_CD` | DOUBLE | NOT NULL |  | The first alias pool code |
| 9 | `A_ALIAS_POOL2_CD` | DOUBLE | NOT NULL |  | The second alias pool code |
| 10 | `A_ALIAS_POOL3_CD` | DOUBLE | NOT NULL |  | The third alias pool code. |
| 11 | `A_ALIAS_TYPE1_CD` | DOUBLE | NOT NULL |  | First alias type code. |
| 12 | `A_ALIAS_TYPE2_CD` | DOUBLE | NOT NULL |  | Second alias type code. |
| 13 | `A_ALIAS_TYPE3_CD` | DOUBLE | NOT NULL |  | Third alias type code. |
| 14 | `A_BIRTH_DT_TM` | DATETIME |  |  | A birth date and time |
| 15 | `A_NAME_FIRST_KEY` | VARCHAR(100) |  |  | A name first key |
| 16 | `A_NAME_FULL` | VARCHAR(100) |  |  | A name full. |
| 17 | `A_NAME_LAST_KEY` | VARCHAR(100) |  |  | A Name Last Key |
| 18 | `A_PERSON_ID` | DOUBLE | NOT NULL | FK→ | a person id |
| 19 | `A_SEX_CD` | DOUBLE | NOT NULL |  | a sex code |
| 20 | `B_ALIAS1` | VARCHAR(200) |  |  | First b alias. |
| 21 | `B_ALIAS2` | VARCHAR(200) |  |  | Second b alias |
| 22 | `B_ALIAS3` | VARCHAR(200) |  |  | Third b alias |
| 23 | `B_ALIAS_POOL1_CD` | DOUBLE | NOT NULL |  | second b alias pool code |
| 24 | `B_ALIAS_POOL2_CD` | DOUBLE | NOT NULL |  | second b alias pool code |
| 25 | `B_ALIAS_POOL3_CD` | DOUBLE | NOT NULL |  | Third b alias pool code. |
| 26 | `B_ALIAS_TYPE1_CD` | DOUBLE | NOT NULL |  | First b alias type code |
| 27 | `B_ALIAS_TYPE2_CD` | DOUBLE | NOT NULL |  | second alias type code |
| 28 | `B_ALIAS_TYPE3_CD` | DOUBLE | NOT NULL |  | Third b alias type code |
| 29 | `B_BIRTH_DT_TM` | DATETIME |  |  | b birth date and time |
| 30 | `B_NAME_FIRST_KEY` | VARCHAR(100) |  |  | b name first key |
| 31 | `B_NAME_FULL` | VARCHAR(100) |  |  | b name full |
| 32 | `B_NAME_LAST_KEY` | VARCHAR(100) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 33 | `B_PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 34 | `B_SEX_CD` | DOUBLE | NOT NULL |  | The gender of the patient (i.e., male, female, unknown). |
| 35 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 36 | `MATCH_DT_TM` | DATETIME |  |  | The date and time when the potential or proposed person match was identified. |
| 37 | `MATCH_REV_FLAG` | DOUBLE |  |  | The flag that determines the match rev. |
| 38 | `MATCH_VAL1_CD` | DOUBLE | NOT NULL |  | First match val code |
| 39 | `MATCH_VAL2_CD` | DOUBLE | NOT NULL |  | Second match value code |
| 40 | `MATCH_VAL3_CD` | DOUBLE | NOT NULL |  | third match val code |
| 41 | `MATCH_VAL4_CD` | DOUBLE | NOT NULL |  | forth match val code |
| 42 | `MATCH_VAL5_CD` | DOUBLE | NOT NULL |  | Fifth match val code |
| 43 | `MATCH_VAL6_CD` | DOUBLE | NOT NULL |  | Sixth match val code |
| 44 | `MATCH_VAL7_CD` | DOUBLE | NOT NULL |  | Seventh match val code |
| 45 | `MATCH_VAL8_CD` | DOUBLE | NOT NULL |  | Eighth match val code |
| 46 | `PERSON_MATCH_REV_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a row on the person-match_rev table. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `A_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `B_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

