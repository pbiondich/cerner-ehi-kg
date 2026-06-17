# PCT_IPASS

> Links Ipass data elements back to a Provider Care Team

**Description:** Physician Care Team Ipass  
**Table type:** ACTIVITY  
**Primary key:** `PCT_IPASS_ID`  
**Columns:** 20  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEGIN_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is considered valid as active current data. This may be valued with the date that the row became active. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | identifies the patient's encounter for which the IPASS data is related to. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `GLOBAL_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the IPASS item should be visible to all providers outside of the care team noted. |
| 6 | `IPASS_DATA_TYPE_CD` | DOUBLE | NOT NULL |  | describes the type of IPASS data contained on that row such as, but not limited to, an action, comment or patient summary |
| 7 | `LAST_UPDT_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person that last updated this row. |
| 8 | `ORIG_PCT_IPASS_ID` | DOUBLE | NOT NULL | FK→ | Used to track versions of the Ipass information. This field will always point back to the original value created. This may be used to find the correct version when combined with the begin and end effective dates and times |
| 9 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The primary key for the row on the table identified by the parent entity name which contains the detailed information for the PCT_IPASS row |
| 10 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The name of the table where the detailed data can be found. |
| 11 | `PCT_CARE_TEAM_ID` | DOUBLE | NOT NULL | FK→ | The Physician Care Team that this Ipass data pertains to. |
| 12 | `PCT_IPASS_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the PCT_IPASS table. |
| 13 | `PCT_SEQ` | DOUBLE | NOT NULL |  | Sequence of row in relation to PCT_TEAM_ID. Only valid when PCT_TEAM_ID > 0. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifies the patient for whom the IPASS data is written. |
| 15 | `POSITION_CD` | DOUBLE | NOT NULL |  | Indicates the role of the user adding or modifying the data. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LAST_UPDT_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ORIG_PCT_IPASS_ID` | [PCT_IPASS](PCT_IPASS.md) | `PCT_IPASS_ID` |
| `PCT_CARE_TEAM_ID` | [PCT_CARE_TEAM](PCT_CARE_TEAM.md) | `PCT_CARE_TEAM_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PCT_IPASS](PCT_IPASS.md) | `ORIG_PCT_IPASS_ID` |

