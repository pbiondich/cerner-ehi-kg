# INVTN_PROGRAM_GROUP_RELTN

> Reference Data. Definition of entities or criteria which make up a program group. This could be a group of locations, patient-provider relationships, etc.

**Description:** INVITATION PROGRAM GROUP RELATION  
**Table type:** REFERENCE  
**Primary key:** `PROGRAM_GROUP_RELTN_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CRITERIA_ID` | DOUBLE | NOT NULL |  | The id of the criteria. A foreign key to the table specified in column CRITERIA_NAME |
| 4 | `CRITERIA_NAME` | VARCHAR(30) | NOT NULL |  | The name of the table the criteria belongs to. Functionally, it specifies the type of the criteria |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `INVTN_VERSION` | DOUBLE | NOT NULL |  | The version of invitation build that this group relation belongs to. |
| 7 | `PREV_PROGRAM_GROUP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Program group relations are grouped by this identifier so that all versions of a program group relation have the same prev_program_group_reltn_id. Type 2 versioning. |
| 8 | `PROGRAM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The program group that this relationship belongs to. |
| 9 | `PROGRAM_GROUP_RELTN_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the program group relation |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PREV_PROGRAM_GROUP_RELTN_ID` | [INVTN_PROGRAM_GROUP_RELTN](INVTN_PROGRAM_GROUP_RELTN.md) | `PROGRAM_GROUP_RELTN_ID` |
| `PROGRAM_GROUP_ID` | [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `PROGRAM_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INVTN_PROGRAM_GROUP_RELTN](INVTN_PROGRAM_GROUP_RELTN.md) | `PREV_PROGRAM_GROUP_RELTN_ID` |

