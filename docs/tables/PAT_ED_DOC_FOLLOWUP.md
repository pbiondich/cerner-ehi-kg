# PAT_ED_DOC_FOLLOWUP

> Store the patients followup information of a document.

**Description:** PAT ED DOC FOLLOWUP  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ADDRESS_TYPE_CD` | DOUBLE | NOT NULL |  | The address type is the code set value which identifies the type of address for the address row (i.e., home, business, etc.) |
| 3 | `ADD_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text id to the address the patient should go to , to see the provider. |
| 4 | `CMT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long_text id to the comments that are provided to patient. |
| 5 | `DAYS_OR_WEEKS` | DOUBLE |  |  | This indicates the days and weeks |
| 6 | `FOLLOWUP_NEEDED_IND` | DOUBLE | NOT NULL |  | An indicator to show if the follow-up needs to happen only "if needed". Follow up with provider only if needed. |
| 7 | `FOL_WITHIN_DAYS` | DOUBLE |  |  | The number of days the patient should follow up. |
| 8 | `FOL_WITHIN_DT_TM` | DATETIME |  |  | %followup% |
| 9 | `FOL_WITHIN_RANGE` | VARCHAR(100) |  |  | Store the date and time range to follow-upin. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Follow up location if the follow up is in a clinic. |
| 11 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Organization used for follow-upinstructions. |
| 12 | `PAT_ED_DOC_FOLLOWUP_ID` | DOUBLE | NOT NULL |  | Primary key .Uniqe id of the follow-up information |
| 13 | `PAT_ED_DOC_ID` | DOUBLE | NOT NULL | FK→ | Identifier to the unique patient education document |
| 14 | `PROVIDER_ID` | DOUBLE | NOT NULL |  | Person id of the provider. |
| 15 | `PROVIDER_NAME` | VARCHAR(4000) |  |  | Name of the provider |
| 16 | `QUICK_PICK_CD` | DOUBLE | NOT NULL |  | Code value of the selected follow-upquick pick selected. |
| 17 | `RECIPIENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Stores the long text ID to the external recipient email |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ADD_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `CMT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PAT_ED_DOC_ID` | [PAT_ED_DOCUMENT](PAT_ED_DOCUMENT.md) | `PAT_ED_DOCUMENT_ID` |
| `RECIPIENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

