# PAT_ED_DOCUMENT

> This table uniquly holds the patient education document for a patients encounter

**Description:** PAT ED DOCUMENT  
**Table type:** ACTIVITY  
**Primary key:** `PAT_ED_DOCUMENT_ID`  
**Columns:** 17  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | Date the document was createdColumn |
| 3 | `CREATE_ID` | DOUBLE | NOT NULL |  | ID of the person that created the documentColumn |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 5 | `EVENT_ID` | DOUBLE | NOT NULL |  | Event Id from the clinical events table after the document is signed . |
| 6 | `PAT_ED_DOCUMENT_ID` | DOUBLE | NOT NULL | PK | Primary key to the tables. uniquely holds the each documents for a encounter |
| 7 | `PAT_ED_DOMAIN_CD` | DOUBLE | NOT NULL |  | This field contains the code value for the patient education domain. A domain is defined as a set of content that is relevant to a clinical context. For instance, the emergency department is a domain that has content that is specific to the ED. And, the acute care domain may have content that is specific to inpatients. |
| 8 | `PAT_ED_SUGGESTED_IND` | DOUBLE |  |  | This determines if the encounter received any patient education instructions that were suggested by emergency medicine algorithm |
| 9 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 10 | `SIGNED_DT_TM` | DATETIME |  |  | This indicated the date n time at which the document is signed. |
| 11 | `SIGNED_ID` | DOUBLE | NOT NULL |  | Signed_id provides the person_id for the prsnl who has signed the document |
| 12 | `STATUS_CD` | DOUBLE | NOT NULL |  | Staus of the document. Code from Code Set 8. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PAT_ED_DOC_ACTIVITY](PAT_ED_DOC_ACTIVITY.md) | `PAT_ED_DOC_ID` |
| [PAT_ED_DOC_FOLLOWUP](PAT_ED_DOC_FOLLOWUP.md) | `PAT_ED_DOC_ID` |
| [PAT_ED_DOC_LEAFLET_ACTIVITY](PAT_ED_DOC_LEAFLET_ACTIVITY.md) | `PAT_ED_DOC_ID` |

