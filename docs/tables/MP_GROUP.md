# MP_GROUP

> Defines the various groups which make up an MPages release or groups which are supplimentary to all MPages releases.

**Description:** MP GROUP  
**Table type:** REFERENCE  
**Primary key:** `MP_GROUP_ID`  
**Columns:** 13  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ARTIFACT_IDENT` | VARCHAR(128) | NOT NULL |  | Corresponds to the Maven identifier for a maven artifact, in this case the component |
| 2 | `BASE_FOLDER` | VARCHAR(255) |  |  | Identifies the cached folder that this file is under in the file system. |
| 3 | `DESCRIPTION` | VARCHAR(255) |  |  | Group Description |
| 4 | `GROUP_IDENT` | VARCHAR(30) | NOT NULL |  | A human-readable identifier for the mp_group row. |
| 5 | `GROUP_TYPE` | VARCHAR(30) |  |  | The type of Group |
| 6 | `MP_GROUP_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `MP_RELEASE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key value from the mp_release table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 13 | `VERSION_TXT` | VARCHAR(30) |  |  | Group Version |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_RELEASE_ID` | [MP_RELEASE](MP_RELEASE.md) | `MP_RELEASE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [MP_COMPONENT](MP_COMPONENT.md) | `MP_GROUP_ID` |
| [MP_GROUP_REFRESH_REQUEST](MP_GROUP_REFRESH_REQUEST.md) | `MP_GROUP_ID` |
| [MP_GROUP_REFRESH_STATE](MP_GROUP_REFRESH_STATE.md) | `MP_GROUP_ID` |
| [MP_UTILITY](MP_UTILITY.md) | `MP_GROUP_ID` |

