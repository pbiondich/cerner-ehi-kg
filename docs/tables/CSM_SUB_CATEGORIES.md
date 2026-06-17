# CSM_SUB_CATEGORIES

> A sub-category id assigned to the sub-category.

**Description:** CSM SUB CATEGORIES  
**Table type:** REFERENCE  
**Primary key:** `CSM_SUB_CAT_ID`  
**Columns:** 9  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_SUB_CAT_DESC` | VARCHAR(40) |  |  | The description is assigned to the sub-category. |
| 2 | `CSM_SUB_CAT_ID` | DOUBLE | NOT NULL | PK | The unique id assigned to the sub-category. |
| 3 | `REQ_TEMPL_ID` | DOUBLE | NOT NULL |  | The unique id of the template assigned to the request sub-category. |
| 4 | `RESL_TEMPL_ID` | DOUBLE | NOT NULL |  | The unique id of the template assigned to the result of the sub-category. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [CSM_CAT_SUB_XREF](CSM_CAT_SUB_XREF.md) | `CSM_SUB_CAT_ID` |
| [CSM_REQUESTS](CSM_REQUESTS.md) | `CSM_SUB_CAT_ID` |
| [CSM_REQUESTS_ARCHIVE](CSM_REQUESTS_ARCHIVE.md) | `CSM_SUB_CAT_ID` |

