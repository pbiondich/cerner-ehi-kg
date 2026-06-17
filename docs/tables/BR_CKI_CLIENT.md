# BR_CKI_CLIENT

> List of clients that use the CKI Mapping wizard. Stores the name, mnemonic and an id.

**Description:** BR CKI Client  
**Table type:** REFERENCE  
**Primary key:** `CLIENT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CLIENT_ID` | DOUBLE | NOT NULL |  | Identifies which bedrock client data belongs to |
| 2 | `CLIENT_ID` | DOUBLE | NOT NULL | PK | Id to identify client specific to cki mapping |
| 3 | `CLIENT_MNEMONIC` | VARCHAR(12) |  |  | Short character string to identify client |
| 4 | `CLIENT_NAME` | VARCHAR(255) |  |  | Long character string to identify client |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [BR_CKI_CLIENT_DATA](BR_CKI_CLIENT_DATA.md) | `CLIENT_ID` |
| [BR_CKI_MATCH](BR_CKI_MATCH.md) | `CLIENT_ID` |

