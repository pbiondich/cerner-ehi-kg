# BR_SETUP_WIZARD

> Used for storing Identifiers created in various identifier setup wizards.

**Description:** Bedrock Setup Wizard  
**Table type:** REFERENCE  
**Primary key:** `BR_SETUP_WIZARD_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BR_SETUP_WIZARD_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_SETUP_WIZARD table. |
| 2 | `SETUP_IDENT` | VARCHAR(20) | NOT NULL |  | Represents an identifier for a site, assigned by an outside agency . A site could be a group of facilities, or a floor of a single facility. It could be a specific ambulatory section, or it could be the entire organization. Can encompass several locations. |
| 3 | `SETUP_NAME` | VARCHAR(150) | NOT NULL |  | The name associated with the setup identifier. |
| 4 | `SETUP_WIZARD_FLAG` | DOUBLE | NOT NULL |  | Identifies the setup wizard associated with an outside agency. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_SETUP_WIZARD_LOC_RELTN](BR_SETUP_WIZARD_LOC_RELTN.md) | `BR_SETUP_WIZARD_ID` |

