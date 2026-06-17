# INVTN_FRAGMENT

> Reference Data. Communication fragments to be pieced together to create an invitation communication.

**Description:** INVITATION FRAGMENT  
**Table type:** REFERENCE  
**Primary key:** `FRAGMENT_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CONTENT_BLOB_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the row on the LONG_BLOB_REFERENCE table with the contents of the fragment. |
| 4 | `CONTENT_TYPE_FLAG` | DOUBLE | NOT NULL |  | Describes what format the fragment is in. |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FRAGMENT_ID` | DOUBLE | NOT NULL | PK | The unique identifier of the fragment |
| 7 | `INVITATION_TYPE` | VARCHAR(50) | NOT NULL |  | The invitation type this fragment is associated to |
| 8 | `METHOD_FLAG` | DOUBLE | NOT NULL |  | The method that this template is for. It currently only applies to templates stored at the program group level.0 = undefined, 1 = printed letter, 2 = IQ health message |
| 9 | `PREV_FRAGMENT_ID` | DOUBLE | NOT NULL | FK→ | Fragments are grouped by this identifier so that all versions of a fragment have the same prev_fragment_id. Type 2 versioning. |
| 10 | `PROGRAM_GROUP_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the INVTN_PROGRAM_GROUP table to identify the program group this fragment is associated to. OPTIONAL: if not populated, then the fragment is at the 'default' level. |
| 11 | `PROGRAM_ID` | DOUBLE | NOT NULL | FK→ | The foreign key to the INVTN_PROGRAM table to identify the program this fragment is associated to. OPTIONAL: only populated for program level or program and status level fragments. |
| 12 | `TRACKING_STATUS_CD` | DOUBLE | NOT NULL |  | The tracking status that this fragment is associated to. OPTIONAL: only populated for program and status level fragments. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CONTENT_BLOB_ID` | [LONG_BLOB_REFERENCE](LONG_BLOB_REFERENCE.md) | `LONG_BLOB_ID` |
| `PREV_FRAGMENT_ID` | [INVTN_FRAGMENT](INVTN_FRAGMENT.md) | `FRAGMENT_ID` |
| `PROGRAM_GROUP_ID` | [INVTN_PROGRAM_GROUP](INVTN_PROGRAM_GROUP.md) | `PROGRAM_GROUP_ID` |
| `PROGRAM_ID` | [INVTN_PROGRAM](INVTN_PROGRAM.md) | `PROGRAM_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [INVTN_FRAGMENT](INVTN_FRAGMENT.md) | `PREV_FRAGMENT_ID` |

