# INVTN_PROGRAM_GROUP

> Reference Data. A logical collection of programs and the attributes that exist for the grouping.

**Description:** INVITATION PROGRAM GROUP  
**Table type:** REFERENCE  
**Primary key:** `PROGRAM_GROUP_ID`  
**Columns:** 25  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `AUTO_GENERATE_IND` | DOUBLE | NOT NULL |  | Determines if the program group should have communications generated automatically according to AUTO_GEN_SCHEDULE. |
| 3 | `AUTO_GEN_CRITERIA_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the LONG_TEXT_REFERENCE table storing the parameters for automatically generating communications for this group. The parameters consist of the invitation list(s) to generate and any filters to apply. The parameters are serialized with JSON. |
| 4 | `AUTO_GEN_DESTINATION` | VARCHAR(50) |  |  | The destination for the communications that are generated automatically. This is likely a back end print queue. |
| 5 | `AUTO_GEN_LAST_SUCCESS_DT_TM` | DATETIME |  |  | The last time communications were successfully generated automatically for this group. |
| 6 | `AUTO_GEN_NEXT_SCHEDULED_DT_TM` | DATETIME |  |  | The next time that communications will automatically be generated for this group. |
| 7 | `AUTO_GEN_SCHEDULE` | VARCHAR(255) |  |  | The schedule determining when to generate communications automatically for this group. Represents the RRule portion of the rfc2445 specification. |
| 8 | `AUTO_GEN_START_DT_TM` | DATETIME |  |  | The first point in time to use the AUTO_GEN_SCHEDULE to generate communications automatically for this group. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `COMMUNICATION_TEMPLATE` | VARCHAR(50) |  |  | The template to use when generating the communication. This is a discern layout program that is client created. |
| 11 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 12 | `INVITATION_TYPE` | VARCHAR(50) | NOT NULL |  | The type of invitation that the program group is for. |
| 13 | `LOOK_BACK_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of time for the look back range. For example: "an encounter within the last 6 months" would be a look back unit of 'months'. |
| 14 | `LOOK_BACK_VALUE` | DOUBLE | NOT NULL |  | A person only qualifies for an invitation for a certain amount of time after a qualifying event. The amount of time that the invitation should exist for this program group is the look_back_value. For example: "an encounter within the last 6 months" would be a look back value of '6'. |
| 15 | `NOTE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The note type that all communications generated for this group will use when they are saved to the patient's chart. Foreign Key to NOTE_TYPE table. |
| 16 | `PREV_PROGRAM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Program groups are grouped by this identifier so that all versions of a program group have the same prev_program_group_id. Type 2 versioning. |
| 17 | `PROGRAM_GROUP_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the program group |
| 18 | `PROGRAM_GROUP_NAME` | VARCHAR(250) | NOT NULL |  | The name of the program group. |
| 19 | `RELEASE_FLAG` | DOUBLE | NOT NULL |  | Identifies the version of the Code Release / RevisionValue 0 - "original" code release.Value 1 - "first" code revision releaseValue 2 - "second" code revision releaseEtc. |
| 20 | `SENDER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel identifier of the user that will be marked as the sender of any invitations sent for this program group |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `AUTO_GEN_CRITERIA_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `NOTE_TYPE_ID` | [NOTE_TYPE](NOTE_TYPE.md) | `NOTE_TYPE_ID` |
| `PREV_PROGRAM_GROUP_ID` | [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `PROGRAM_GROUP_ID` |
| `SENDER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [INVTN_FRAGMENT](INVTN_FRAGMENT.md) | `PROGRAM_GROUP_ID` |
| [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_GROUP_ID` |
| [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `PREV_PROGRAM_GROUP_ID` |
| [INVTN_PROGRAM_GROUP_RELTN](INVTN_PROGRAM_GROUP_RELTN.md) | `PROGRAM_GROUP_ID` |

