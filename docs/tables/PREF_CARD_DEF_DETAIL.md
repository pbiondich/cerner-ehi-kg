# PREF_CARD_DEF_DETAIL

> Contains the values associated with preference card default entries

**Description:** Preference Card Default Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 2 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted on the table |
| 3 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 4 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 5 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the long_text table indicating the text associated with this preference card default. This column is only populated if the accept length for the default detail is greater than 200 (defined in the Form Builder Design and Test Tool). |
| 6 | `PREF_CARD_DEF_DETAIL_ID` | DOUBLE | NOT NULL |  | The primary key, uniquely identifying a preference card default value. |
| 7 | `PREF_CARD_DEF_ID` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the pref_card_default table indicating the entry associated with this preference card default value. |
| 8 | `PREF_CARD_DEF_TEXT_SEQ` | DOUBLE |  |  | The sequence of a default value for repeating input controls. This column is only populated for free-text input controls. |
| 9 | `PREF_CARD_DEF_VALUE` | VARCHAR(200) |  |  | The value associated with this preference card default |
| 10 | `PREF_CARD_DEF_VALUE_SEQ` | DOUBLE |  |  | The sequence of this preference card default value (for repeating input controls). |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREF_CARD_DEF_ID` | [PREF_CARD_DEFAULT](PREF_CARD_DEFAULT.md) | `PREF_CARD_DEF_ID` |

