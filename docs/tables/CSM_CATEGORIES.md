# CSM_CATEGORIES

> This table is the beginning stage of building the client services database.

**Description:** Categories are high level groupings for client service requests.  
**Table type:** REFERENCE  
**Primary key:** `CSM_CAT_ID`  
**Columns:** 7  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_CAT_DESC` | CHAR(40) | NOT NULL |  | The description given to the category, limit of 40 characters. |
| 2 | `CSM_CAT_ID` | DOUBLE | NOT NULL | PK | The unique identifier given to the category. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [CSM_CAT_SUB_XREF](CSM_CAT_SUB_XREF.md) | `CSM_CAT_ID` |
| [CSM_Q_CAT_XREF](CSM_Q_CAT_XREF.md) | `CSM_CAT_ID` |
| [CSM_REQUESTS](CSM_REQUESTS.md) | `CSM_CAT_ID` |
| [CSM_REQUESTS_ARCHIVE](CSM_REQUESTS_ARCHIVE.md) | `CSM_CAT_ID` |

