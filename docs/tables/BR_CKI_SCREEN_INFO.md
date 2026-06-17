# BR_CKI_SCREEN_INFO

> Stores the display value for columns in the CKI Mapping Wizard

**Description:** Bedrock CKI Screen Info  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `DATA_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Id for the data type |
| 3 | `SCREEN_DISPLAY` | VARCHAR(60) |  |  | Display value for the column |
| 4 | `SCREEN_INFO_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 5 | `SCREEN_POSITION` | DOUBLE |  |  | Order to be displayed for the display values on the screen of the wizard. |
| 6 | `SCREEN_TYPE` | VARCHAR(30) |  |  | String for the page in the CKI Wizard |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DATA_TYPE_ID` | [BR_CKI_DATA_TYPE](BR_CKI_DATA_TYPE.md) | `DATA_TYPE_ID` |

