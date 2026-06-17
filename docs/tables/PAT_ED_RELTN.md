# PAT_ED_RELTN

> Contains the relationship between the individual instructions and the instruction hierarchy

**Description:** Patient Education Relationship table  
**Table type:** REFERENCE  
**Primary key:** `PAT_ED_RELTN_ID`  
**Columns:** 23  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTENT_SUPPLIER_CD` | DOUBLE | NOT NULL |  | Content Supplier Code |
| 3 | `CUSTOM_IND` | DOUBLE | NOT NULL |  | 0 - Indicates the row is Standard Content 1 - Indicates the row is a Custom Instruction |
| 4 | `DOC_LANG_ID_VALUE` | DOUBLE | NOT NULL |  | Language identifier that corresponds to the language of the instruction. This is storing an id that relates to the language for the instruction content. |
| 5 | `DOC_TYPES` | VARCHAR(255) |  |  | A list of document types that this instruction content is related to. Relates the instruction to different document types. |
| 6 | `KEY_DOC_IDENT` | VARCHAR(255) |  |  | Indicates content provider unique instruction key identifier |
| 7 | `KEY_DOC_ID_VALUE` | DOUBLE | NOT NULL |  | Unique key identifier per content domain. This is storing an identifier - unique to an instruction and content domain used. Value comes from an outside source. |
| 8 | `PAT_ED_DOMAIN_CD` | DOUBLE | NOT NULL |  | This field contains the code value for the patient education domain. A domain is defined as a set of content that is relevant to a clinical context. For instance, the emergency department is a domain that has content that is specific to the ED. And, the acute care domain may have content that is specific to inpatients. |
| 9 | `PAT_ED_RELTN_DESC` | VARCHAR(1000) |  |  | This is the Title of the Instruction that is displayed in the hierarchy. |
| 10 | `PAT_ED_RELTN_DESC_KEY` | VARCHAR(1000) | NOT NULL |  | INDEXED FIELD for the Title of the Instruction that is displayed in the hierarchy. |
| 11 | `PAT_ED_RELTN_DESC_KEY_A_NLS` | VARCHAR(4000) |  |  | PAT_ED_RELTN_DESC_KEY_A_NLS column |
| 12 | `PAT_ED_RELTN_DESC_KEY_NLS` | VARCHAR(2002) |  |  | Corresponding Non-English character set for the Title of the Instruction that is displayed in the hierarchy. (no longer used - replaced by the _A_NLS version of this column). |
| 13 | `PAT_ED_RELTN_ID` | DOUBLE | NOT NULL | PK | Identifier used to uniquely identify Patient Education Relation records. |
| 14 | `PAT_ED_RELTN_PARENT_ID` | DOUBLE | NOT NULL | FK→ | Parent PAT_ED_RELTN_ID to this row used to define the hierarchy of instructions |
| 15 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel ID from the PRSNL table that identifies the owner of the custom instruction. PRNSL_ID of 0 indicates public instruction. |
| 16 | `REFR_TEXT_ID` | DOUBLE | NOT NULL |  | As of early 2007 - This column now contains a foreign key value from the LONG_BLOB_REFERENCE table. That is when patient education content began to incorporate images. As a result, long_text_reference no longer had the capacity to save an entire document |
| 17 | `SHORTCUT_NAME` | VARCHAR(1000) |  |  | This column will become obsolete when new table (PAT_ED_SHORTCUT) is implemented. New logic allows for multiple shortcut names -- shortcut name of an instruction that is given by the content domain. |
| 18 | `TRACK_GROUP_CD` | DOUBLE | NOT NULL |  | Identifies the TRACK_GROUP_CD for Instructions |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PAT_ED_RELTN_PARENT_ID` | [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [MRU_LOOKUP_ED_DOC](MRU_LOOKUP_ED_DOC.md) | `PAT_ED_RELTN_ID` |
| [PAT_ED_DOC_ACTIVITY](PAT_ED_DOC_ACTIVITY.md) | `PAT_ED_RELTN_ID` |
| [PAT_ED_FAVORITES](PAT_ED_FAVORITES.md) | `PAT_ED_RELTN_ID` |
| [PAT_ED_RELTN](PAT_ED_RELTN.md) | `PAT_ED_RELTN_PARENT_ID` |
| [PAT_ED_SHORTCUT](PAT_ED_SHORTCUT.md) | `PAT_ED_RELTN_ID` |

