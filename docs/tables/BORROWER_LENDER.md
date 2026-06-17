# BORROWER_LENDER

> The Borrower_Lender table contains those persons and places that either borrow or lend films/folders within image management applications.

**Description:** Borrower Lender  
**Table type:** REFERENCE  
**Primary key:** `BORROWER_LENDER_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BORROWER_LENDER_ID` | DOUBLE | NOT NULL | PK | The Borrower_Lender_Id uniquely identifies a row within the Borrower_Lender table. It has no other meaning or purpose other than to serve as a unique id. |
| 3 | `BORROWER_LENDER_IND` | DOUBLE | NOT NULL |  | The Borrower_Lender_Ind indicates if this entry is a borrower or a lender. |
| 4 | `CONTACT_NAME` | VARCHAR(100) |  |  | If the borrower or lender is a place, rather than a person, then this contains the name of the person to contact at that site. |
| 5 | `MAIL_NAME` | VARCHAR(100) |  |  | The Mail_Name contains the name of the borrower or lender formatted the way that it should print on letters and labels. |
| 6 | `NAME` | VARCHAR(100) |  |  | The Name contains the name of the borrower or lender formatted the way that is should appear in a pick list. |
| 7 | `NAME_KEY` | VARCHAR(100) | NOT NULL |  | The Name_Key contains the value of the name field in all caps. This field exists only for search capability, it will never be viewed. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_REQUEST](RAD_REQUEST.md) | `LENDER_ID` |

