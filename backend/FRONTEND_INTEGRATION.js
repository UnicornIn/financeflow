// Frontend Integration Examples
// Use these examples in your frontend to interact with the backend API

const API_BASE_URL = "http://localhost:8000/api/v1";

// ============================================
// AUTHENTICATION ENDPOINTS
// ============================================

/**
 * Register a new user
 */
export async function registerUser(email, password, fullName) {
  const response = await fetch(`${API_BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email,
      password,
      full_name: fullName
    })
  });
  const data = await response.json();
  if (response.ok) {
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("user_id", data.user_id);
    return data;
  }
  throw new Error(data.detail);
}

/**
 * Login user
 */
export async function loginUser(email, password) {
  const response = await fetch(`${API_BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });
  const data = await response.json();
  if (response.ok) {
    localStorage.setItem("token", data.access_token);
    localStorage.setItem("user_id", data.user_id);
    return data;
  }
  throw new Error(data.detail);
}

/**
 * Get current user info
 */
export async function getCurrentUser() {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/auth/me`, {
    method: "GET",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return await response.json();
}

/**
 * Refresh token
 */
export async function refreshToken() {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/auth/refresh-token`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${token}` }
  });
  const data = await response.json();
  if (response.ok) {
    localStorage.setItem("token", data.access_token);
    return data;
  }
  throw new Error(data.detail);
}

// ============================================
// USER ENDPOINTS
// ============================================

/**
 * Get user by ID
 */
export async function getUser(userId) {
  const response = await fetch(`${API_BASE_URL}/users/${userId}`);
  return await response.json();
}

/**
 * Update user
 */
export async function updateUser(userId, data) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(data)
  });
  return await response.json();
}

/**
 * Delete user
 */
export async function deleteUser(userId) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/users/${userId}`, {
    method: "DELETE",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return await response.json();
}

// ============================================
// STREAK ENDPOINTS
// ============================================

/**
 * Get user streak
 */
export async function getStreak(userId) {
  const response = await fetch(`${API_BASE_URL}/streaks/${userId}`);
  return await response.json();
}

/**
 * Increment streak (when user completes activity)
 */
export async function incrementStreak(userId) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/streaks/${userId}/increment`, {
    method: "POST",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return await response.json();
}

/**
 * Get leaderboard
 */
export async function getLeaderboard(limit = 10) {
  const response = await fetch(`${API_BASE_URL}/streaks/leaderboard/top?limit=${limit}`);
  return await response.json();
}

// ============================================
// PROFILE ENDPOINTS
// ============================================

/**
 * Get user profile
 */
export async function getProfile(userId) {
  const response = await fetch(`${API_BASE_URL}/profiles/${userId}`);
  return await response.json();
}

/**
 * Submit quiz answers
 */
export async function submitQuiz(answers) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/profiles/quiz/submit`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({ answers })
  });
  return await response.json();
}

/**
 * Update user profile
 */
export async function updateProfile(userId, profileData) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/profiles/${userId}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify(profileData)
  });
  return await response.json();
}

// ============================================
// CHAT ENDPOINTS
// ============================================

/**
 * Send chat message
 */
export async function sendMessage(text, chatTitle = null) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/chat/message`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({
      title: chatTitle,
      text: text
    })
  });
  return await response.json();
}

/**
 * Get chat history
 */
export async function getChatHistory(conversationId) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/chat/${conversationId}/history`, {
    method: "GET",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return await response.json();
}

/**
 * Delete conversation
 */
export async function deleteConversation(conversationId) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/chat/${conversationId}`, {
    method: "DELETE",
    headers: { "Authorization": `Bearer ${token}` }
  });
  return await response.json();
}

// ============================================
// GAME ENDPOINTS
// ============================================

/**
 * Get all scenarios
 */
export async function getScenarios(limit = 10) {
  const response = await fetch(`${API_BASE_URL}/games/scenarios?limit=${limit}`);
  return await response.json();
}

/**
 * Get specific scenario with explanation
 */
export async function getScenario(scenarioId) {
  const response = await fetch(`${API_BASE_URL}/games/scenarios/${scenarioId}`);
  return await response.json();
}

/**
 * Submit game response
 */
export async function submitGameResponse(scenarioId, userAnswer) {
  const token = localStorage.getItem("token");
  const response = await fetch(`${API_BASE_URL}/games/responses`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${token}`
    },
    body: JSON.stringify({
      scenario_id: scenarioId,
      user_answer: userAnswer
    })
  });
  return await response.json();
}

// ============================================
// CONCEPT ENDPOINTS
// ============================================

/**
 * Get all concepts
 */
export async function getConcepts(limit = 50) {
  const response = await fetch(`${API_BASE_URL}/concepts?limit=${limit}`);
  return await response.json();
}

/**
 * Get specific concept
 */
export async function getConcept(conceptId) {
  const response = await fetch(`${API_BASE_URL}/concepts/${conceptId}`);
  return await response.json();
}

/**
 * Search concepts
 */
export async function searchConcepts(query) {
  const response = await fetch(`${API_BASE_URL}/concepts/search?q=${encodeURIComponent(query)}`);
  return await response.json();
}

/**
 * Get concepts by category
 */
export async function getConceptsByCategory(category) {
  const response = await fetch(`${API_BASE_URL}/concepts/category/${category}`);
  return await response.json();
}

// ============================================
// USAGE EXAMPLES
// ============================================

/*
// Example 1: User Registration & Login Flow
async function exampleAuthFlow() {
  try {
    // Register
    const registerData = await registerUser("user@example.com", "password123", "John Doe");
    console.log("Registered:", registerData);
    
    // Get current user
    const user = await getCurrentUser();
    console.log("Current user:", user);
    
  } catch (error) {
    console.error("Auth error:", error);
  }
}

// Example 2: Get concepts and scenarios
async function exampleGetContent() {
  const concepts = await getConcepts(10);
  console.log("Concepts:", concepts);
  
  const scenarios = await getScenarios(5);
  console.log("Scenarios:", scenarios);
}

// Example 3: Play a game scenario
async function exampleGameFlow() {
  const scenarios = await getScenarios(1);
  const scenario = scenarios[0];
  
  // Get full scenario with explanation
  const full = await getScenario(scenario.id);
  console.log("Scenario:", full);
  
  // Submit answer
  const response = await submitGameResponse(scenario.id, 1);
  console.log("Answer result:", response);
  
  // Increment streak if correct
  if (response.is_correct) {
    const userId = localStorage.getItem("user_id");
    const streak = await incrementStreak(userId);
    console.log("Updated streak:", streak);
  }
}

// Example 4: Chat with assistant
async function exampleChatFlow() {
  const msg = await sendMessage("How do I start budgeting?", "Financial Questions");
  console.log("Chat created:", msg);
  
  const history = await getChatHistory(msg.chat_id);
  console.log("Chat history:", history);
}
*/
