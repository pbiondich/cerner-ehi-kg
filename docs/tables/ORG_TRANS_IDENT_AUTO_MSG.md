# ORG_TRANS_IDENT_AUTO_MSG

> This table is used to store additional information about automated messaging for identifiers necessary to submit transactions for an organization.

**Description:** Organization Transaction Identifiers Automated Messaging  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ORG_FOLDER_LOCATION_PATH` | VARCHAR(100) | NOT NULL |  | This is the folder location that the file needs to be transferred to for automated messaging. |
| 2 | `ORG_PARTNER_IDENT` | VARCHAR(100) | NOT NULL |  | This is the identifier of the partner associated with the automated messaging. |
| 3 | `ORG_SFTP_LOCATION_PATH` | VARCHAR(100) | NOT NULL |  | This is the SFTP location that the file needs to be transferred to for automated messaging. |
| 4 | `ORG_TRANS_IDENT_AUTO_MSG_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 5 | `ORG_TRANS_IDENT_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ORG_TRANS_INDENT_AUTO_MSG. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORG_TRANS_IDENT_ID` | [ORG_TRANS_IDENT](ORG_TRANS_IDENT.md) | `ORG_TRANS_IDENT_ID` |

