# CSM_REQUESTS

> This table is the actual ordered requests.

**Description:** CSM REQUESTS  
**Table type:** ACTIVITY  
**Primary key:** `CSM_REQ_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CSM_CAT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the category |
| 2 | `CSM_COMPL_DT_TM` | DATETIME |  |  | The completion date/time of the request. |
| 3 | `CSM_CURRENT_USER` | CHAR(50) |  |  | Shows the current user when the request is being edited in the CSM Request Viewer |
| 4 | `CSM_DUE_DT_TM` | DATETIME |  |  | The due date/time of the request. |
| 5 | `CSM_ORD_DT_TM` | DATETIME |  |  | Date and time that the service request was ordered. |
| 6 | `CSM_PRIOR_ID` | DOUBLE | NOT NULL | FK→ | Unique priority id |
| 7 | `CSM_REQ_COM_ID` | DOUBLE | NOT NULL | FK→ | long text id for the request comments |
| 8 | `CSM_REQ_ID` | DOUBLE | NOT NULL | PK | The unique id for the request. |
| 9 | `CSM_RSLT_COM_ID` | DOUBLE | NOT NULL | FK→ | long text id for the result comments |
| 10 | `CSM_SUB_CAT_ID` | DOUBLE | NOT NULL | FK→ | Unique Sub-Category ID |
| 11 | `LOCATION_CD` | DOUBLE | NOT NULL |  | location code for the ordering location |
| 12 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization id for the ordering organization |
| 13 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier for the phone number |
| 14 | `PROBLEM_REQ_COMMENT_ID` | DOUBLE | NOT NULL | FK→ | Contains the problem requisition comment identifier to relate this request to the appropriate long text string. |
| 15 | `SELECTED_PHONE_ID` | DOUBLE | NOT NULL | FK→ | Phone ID for the currently selected phone number |
| 16 | `STATUS_CD` | DOUBLE | NOT NULL |  | code value for the service request status |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CSM_CAT_ID` | [CSM_CATEGORIES](CSM_CATEGORIES.md) | `CSM_CAT_ID` |
| `CSM_PRIOR_ID` | [CSM_PRIORITIES](CSM_PRIORITIES.md) | `CSM_PRIOR_ID` |
| `CSM_REQ_COM_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CSM_RSLT_COM_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CSM_SUB_CAT_ID` | [CSM_SUB_CATEGORIES](CSM_SUB_CATEGORIES.md) | `CSM_SUB_CAT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |
| `PROBLEM_REQ_COMMENT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `SELECTED_PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CSM_LST_CONTACT](CSM_LST_CONTACT.md) | `CSM_REQ_ID` |

