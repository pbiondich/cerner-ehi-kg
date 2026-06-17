# DMS_MEDIA_OWNERSHIP

> Contains media ownership keys that relate to media objects.

**Description:** Digital Media Services Media Ownership  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 8

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DMS_MEDIA_IDENTIFIER_ID` | DOUBLE | NOT NULL | FK→ | The ID of the row in the DMS_MEDIA_IDENTIFIER table that the ownership key relates to. |
| 2 | `DMS_MEDIA_OWNERSHIP_ID` | DOUBLE | NOT NULL |  | The primary key of the DMS_MEDIA_OWNERSHIP table. |
| 3 | `OWNERSHIP_UUID` | VARCHAR(255) | NOT NULL |  | Contains the ownership key. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DMS_MEDIA_IDENTIFIER_ID` | [DMS_MEDIA_IDENTIFIER](DMS_MEDIA_IDENTIFIER.md) | `DMS_MEDIA_IDENTIFIER_ID` |

