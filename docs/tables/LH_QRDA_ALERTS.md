# LH_QRDA_ALERTS

> This table is used to store elements that are used to create the Alerts Section in the body of a QRDA file for submission

**Description:** LH_QRDA_ALERTS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 29

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALERT_ID` | DOUBLE | NOT NULL |  | Unique alert id |
| 2 | `ALLERGY_STATUS_CD` | VARCHAR(50) |  |  | The code associated with an allergy |
| 3 | `ALLERGY_STATUS_CD_SYSTEM` | VARCHAR(50) |  |  | Represents the codeSystem string of the observation/code/@codesystem |
| 4 | `EXTRACT_DT_TM` | DATETIME |  |  | The date/time that the record was extracted from the source system. |
| 5 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the first ETL process started that created this record. |
| 6 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Identifies the delivery network responsible for supplying the data. |
| 7 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Identifies the unique source within the delivery network responsible for supplying the data. |
| 8 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | The date/time that the last ETL process started that updated this record. |
| 9 | `LH_QRDA_ALERTS_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the LH_QRDA_ALERTS table. |
| 10 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL |  | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 11 | `NEGATION_IND` | DOUBLE |  |  | Indicates whether a negation exists or not |
| 12 | `ONSET_DT_TM` | DATETIME |  |  | Indicates the timing of the concern |
| 13 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The value of the primary identifier of the table to which the Problem section is related (i.e. lh_qrda_pqrs_id) |
| 14 | `PARENT_ENTITY_ID2` | DOUBLE | NOT NULL |  | The value of the primary identifier of millennium source table |
| 15 | `PARENT_ENTITY_NAME` | VARCHAR(50) | NOT NULL |  | The name of the table this Problem section is related (i.e. LH_QRDA_PQRS) |
| 16 | `PARENT_ENTITY_NAME2` | VARCHAR(50) |  |  | The name of millennium source table |
| 17 | `PARTICIPANT_CD` | VARCHAR(50) |  |  | The value for participant / participantRole / playingEntity / code SHALL be selected from the Appendix_H-Alerts tab of the Downloadable Resources table. |
| 18 | `PARTICIPANT_CD_DISPLAY` | VARCHAR(500) |  |  | String representation of Participant Code |
| 19 | `PARTICIPANT_CD_SYSTEM` | VARCHAR(50) |  |  | Represents the codeSystem string of the observation/code/@codesystem |
| 20 | `PARTICIPANT_CD_SYSTEM_NAME` | VARCHAR(100) |  |  | Description of Participant_CD's OID system |
| 21 | `REACTION_CD` | VARCHAR(50) |  |  | The value for Observation / statusCode in a reaction observation SHALL be completed 2.16.840.1.113883.5.14 ActStatus STATIC. |
| 22 | `REACTION_CD_SYSTEM` | VARCHAR(50) |  |  | Coding system used for the given reaction_cd. |
| 23 | `SEVERITY_CD` | VARCHAR(50) |  |  | The value for Observation / code in a severity observation SHALL be SEV Severity observation 2.16.840.1.113883.5.4 ActCode STATIC. |
| 24 | `SEVERITY_CD_SYSTEM` | VARCHAR(50) |  |  | Coding system used for the given severity_cd. |
| 25 | `SEVERITY_VALUE` | VARCHAR(50) |  |  | Value representing the severity. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_SOURCE` | VARCHAR(50) | NOT NULL |  | The script name responsible for updating the record. |
| 29 | `UPDT_TASK` | VARCHAR(50) | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

