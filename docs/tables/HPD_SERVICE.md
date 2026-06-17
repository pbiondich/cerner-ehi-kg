# HPD_SERVICE

> Stores the provider's available service information (i.e. email address).

**Description:** Healthcare Provider Directory Service  
**Table type:** REFERENCE  
**Primary key:** `HPD_SERVICE_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EMAIL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of Email - code value from code set 43 - will have CDF Meaning EXTSECEMAIL or INTSECEMAIL . |
| 3 | `FORMATTED_DISPLAY_NAME` | VARCHAR(255) |  |  | The Formatted Display Name used for the service email address |
| 4 | `HPD_SERVICE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `REVISION_NBR` | DOUBLE | NOT NULL |  | Current revision of the table. This should be incremented 1 higher than the highest revision on the table. All rows in the same update should have the same revision. |
| 6 | `SERVICE_EMAIL_ADDRESS` | VARCHAR(255) | NOT NULL |  | E-mail Address |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HPD_MEMBER_SERVICE_RELTN](HPD_MEMBER_SERVICE_RELTN.md) | `HPD_SERVICE_ID` |

