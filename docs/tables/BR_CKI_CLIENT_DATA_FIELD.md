# BR_CKI_CLIENT_DATA_FIELD

> Stores client data fields for the BR_CKI_CLINENT_DATA table

**Description:** BR CKI CLIENT DATA FIELDS  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_CKI_CLIENT_DATA_FIELD_ID` | DOUBLE | NOT NULL |  | Unique id for the table |
| 2 | `BR_CKI_CLIENT_DATA_ID` | DOUBLE | NOT NULL | FK→ | Unique id for the parent table |
| 3 | `FIELD_CONTENT` | VARCHAR(100) |  |  | Client data loaded from a spreadsheet. Will vary by data type. (Descriptions, Mnemonics, CPT4, filters, etc?) |
| 4 | `FIELD_NBR` | DOUBLE | NOT NULL |  | Field number to sequence or order the fields for client data |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_CKI_CLIENT_DATA_ID` | [BR_CKI_CLIENT_DATA](BR_CKI_CLIENT_DATA.md) | `BR_CKI_CLIENT_DATA_ID` |

