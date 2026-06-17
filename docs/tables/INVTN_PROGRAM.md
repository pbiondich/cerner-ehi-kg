# INVTN_PROGRAM

> Programs provide a defined scope for a group of invitations. All invitations belong to exactly one program.

**Description:** Includes all programs that have been built for invitations.  
**Table type:** REFERENCE  
**Primary key:** `PROGRAM_ID`  
**Columns:** 17  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `PREV_PROGRAM_ID` | DOUBLE | NOT NULL | FK→ | Programs are grouped by this identifier so that all versions of a program have the same prev_program_id. Type 2 versioning. |
| 5 | `PROGRAM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the INVTN_PROGRAM_GROUP table to identify which group the program belongs to. |
| 6 | `PROGRAM_ID` | DOUBLE | NOT NULL | PK | The unique primary key that identifies the program. |
| 7 | `PROGRAM_MEANING` | VARCHAR(100) | NOT NULL |  | Represents the unique meaning for the program. |
| 8 | `PROGRAM_NAME` | VARCHAR(250) | NOT NULL |  | The display name of the program. This is typically unique within a program group. |
| 9 | `PROGRAM_TYPE` | VARCHAR(100) | NOT NULL |  | Represents the type of program that contains the invitation. |
| 10 | `SOURCE_MEANING` | VARCHAR(250) | NOT NULL |  | The meaning of the SOURCE of the program. This must be unique per program_group_id and source_type. |
| 11 | `SOURCE_TYPE` | VARCHAR(100) | NOT NULL |  | The type of the SOURCE of the program |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 17 | `WORKFLOW_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the INVTN_WORKFLOW table to identify which workflow is associated to the program. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_PROGRAM_ID` | [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_ID` |
| `PROGRAM_GROUP_ID` | [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `PROGRAM_GROUP_ID` |
| `WORKFLOW_ID` | [INVTN_WORKFLOW](INVTN_WORKFLOW.md) | `WORKFLOW_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [INVTN_COMMUNICATION](INVTN_COMMUNICATION.md) | `PROGRAM_ID` |
| [INVTN_FRAGMENT](INVTN_FRAGMENT.md) | `PROGRAM_ID` |
| [INVTN_INVITATION](INVTN_INVITATION.md) | `PROGRAM_ID` |
| [INVTN_INVITATION_ACTION](INVTN_INVITATION_ACTION.md) | `PROGRAM_ID` |
| [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PREV_PROGRAM_ID` |

